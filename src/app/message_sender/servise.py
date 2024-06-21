import aiohttp

from ..schemas.schema import Message, Subscription


async def send_message_to_subscription(message: Message, subscription: Subscription):
    async with (aiohttp.ClientSession() as session):
        async with session.post(
                url=subscription.url,
                json=message.model_dump()
        ) as response:
            assert response.status == aiohttp.http.HTTPStatus.OK, (
                f"Can't send message to {subscription.model_dump()}"
                f" with status {response.status}"
            )

