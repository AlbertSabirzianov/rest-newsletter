import json

import aioredis

from ..schemas.schema import Message
from ..settings.settings import redis_settings


class RedisConnector:

    def __init__(self):
        self.redis = aioredis.from_url(redis_settings.redis_url)
        self.pubsub = self.redis.pubsub()
        self.is_subscribe = False

    async def send_new_message(self, message: Message):
        if not self.is_subscribe:
            await self.pubsub.subscribe(redis_settings.chanel_name)
            self.is_subscribe = True
        await self.redis.publish(
            redis_settings.chanel_name,
            json.dumps(message.model_dump())
        )


redis_connector = RedisConnector()

