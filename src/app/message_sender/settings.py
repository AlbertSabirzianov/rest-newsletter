from pydantic_settings import BaseSettings


class MessageSettings(BaseSettings):
    is_repeat_sending: bool = False
    timeout_to_repeat_in_seconds: int = 30


message_settings = MessageSettings()
