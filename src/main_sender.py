import logging

from app.message_sender.message_sender import message_sender

logging.basicConfig(
    filename='data/logs.log',
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
    format="%(asctime)s - %(module)s - %(levelname)s - %(message)s"
)


if __name__ == "__main__":
    message_sender.run()

