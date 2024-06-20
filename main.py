import asyncio

from src.extensions import message_queue
from src.message_sender.message_sender import MessageSender


async def main():
    message_sender = MessageSender(message_queue)
    await asyncio.gather(
        message_sender.run()
    )


if __name__ == "__main__":
    asyncio.run(main())

