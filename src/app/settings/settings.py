from pydantic_settings import BaseSettings


class RedisSettings(BaseSettings):
    redis_url: str = "redis://redis"
    chanel_name: str = "new_message"


redis_settings = RedisSettings()

