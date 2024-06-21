import asyncio
import datetime

import aiohttp

from src.app.schemas.schema import Message, Subscription, SendingError
from src.app.repositories.subscription_repository import subscription_repository
from src.app.repositories.sending_error_repository import sending_error_repository
from .servise import send_message_to_subscription
from .settings import message_settings


class MessageSender:

    def __init__(self, message_queue: asyncio.Queue):
        self.message_queue: asyncio.Queue[Message] = message_queue
        self.repeat_queue: asyncio.Queue[Message] = asyncio.Queue()

    async def repeat_send(self):
        while True:
            message = await self.repeat_queue.get()
            await asyncio.sleep(message_settings.timeout_to_repeat_in_seconds)
            await self.message_queue.put(message)

    async def send(self):
        while True:
            message = await self.message_queue.get()
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

    async def run(self):
        await asyncio.gather(
            self.send(),
            self.repeat_send()
        )

