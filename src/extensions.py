from asyncio import Queue

from .schemas.schema import Message

message_queue: Queue[Message] = Queue()

