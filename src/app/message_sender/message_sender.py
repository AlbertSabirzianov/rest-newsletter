import asyncio
import datetime
import json
import logging

import aiohttp
import aioredis

from .servise import send_message_to_subscription
from .settings import message_settings
from ..repositories.sending_error_repository import sending_error_repository
from ..repositories.subscription_repository import subscription_repository
from ..schemas.schema import Message, Subscription, SendingError
from ..settings.settings import redis_settings


class MessageSender:

    def __init__(self):
        self.send_queue: asyncio.Queue[Message] = asyncio.Queue()
        self.repeat_queue: asyncio.Queue[Message] = asyncio.Queue()

    async def repeat_send(self):
        while True:
            message = await self.repeat_queue.get()
            await asyncio.sleep(message_settings.timeout_to_repeat_in_seconds)
            await self.send_queue.put(message)

    async def send(self):
        while True:
            message = await self.send_queue.get()
            subscriptions: list[Subscription] = subscription_repository.get_subscriptions_by_subject_name(
                message.subject_name
            )
            for subscription in subscriptions:
                try:
                    await send_message_to_subscription(
                        message=message,
                        subscription=subscription
                    )
                except (AssertionError, aiohttp.ClientError) as err:
                    sending_error_repository.set_object(
                        SendingError(
                            subscription=subscription,
                            message=message,
                            description=str(err),
                            time=datetime.datetime.now()
                        )
                    )
                    if message_settings.is_repeat_sending:
                        await self.repeat_queue.put(message)

    async def listen_new_messages(self):
        redis = await aioredis.from_url(redis_settings.redis_url)
        pubsub = redis.pubsub()
        await pubsub.subscribe(redis_settings.chanel_name)
        while True:
            new_message = await pubsub.get_message(ignore_subscribe_messages=True)
            if new_message:
                logging.warning(str(new_message))
                await self.send_queue.put(
                    Message(**json.loads(new_message["data"]))
                )

    def run(self):
        loop = asyncio.get_event_loop()
        loop.create_task(self.listen_new_messages())
        loop.create_task(self.send())
        loop.create_task(self.repeat_send())
        loop.run_forever()


message_sender = MessageSender()

