from pydantic_settings import BaseSettings


class RedisSettings(BaseSettings):
    redis_url: str = "redis://redis"
    chanel_name: str = "new_message"


class MessageSettings(BaseSettings):
    is_repeat_sending: bool = False
    timeout_to_repeat_in_seconds: int = 30


message_settings = MessageSettings()
redis_settings = RedisSettings()

