from pydantic_settings import BaseSettings


class RedisSettings(BaseSettings):
    redis_url: str = "redis://redis"

