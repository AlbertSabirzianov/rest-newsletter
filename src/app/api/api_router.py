from typing import List

from fastapi import APIRouter, Response, status


from ..repositories.sending_error_repository import sending_error_repository
from ..repositories.subjects_repository import subject_repository
from ..repositories.subscription_repository import subscription_repository
from ..schemas.schema import Message, Subscription, Subject, SendingError
from .utils import ALREADY_EXISTS, NOT_EXISTS, CREATED, DELETED

api_router = APIRouter()


# subjects
@api_router.get("/subjects", response_model=List[Subject])
def get_all_subjects():
    return subject_repository.get_all_objects()


@api_router.delete("/subjects/{subject_name}")
def delete_subject(subject_name: str, response: Response):
    if not subject_repository.get_subject_by_name(subject_name):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return NOT_EXISTS
    subject_repository.delete_subject_by_name(subject_name)
    subscription_repository.delete_subscriptions_by_subject_name(subject_name)
    return DELETED


@api_router.post("/subjects")
def post_subject(subject: Subject, response: Response):
    if subject_repository.get_subject_by_name(subject.name):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return ALREADY_EXISTS
    subject_repository.set_object(subject)
    response.status_code = status.HTTP_201_CREATED
    return CREATED


# subscriptions
@api_router.get("/subscriptions", response_model=List[Subscription])
def get_subscriptions():
    return subscription_repository.get_all_objects()


@api_router.post("/subscriptions")
def post_subscription(subscription: Subscription, response: Response):
    if not subject_repository.get_subject_by_name(subscription.subject_name):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return NOT_EXISTS
    if subscription in subscription_repository.objects:
        return ALREADY_EXISTS
    subscription_repository.set_object(subscription)
    return CREATED


@api_router.delete("/subscriptions")
def delete_subscription(subscription: Subscription):
    if subscription not in subscription_repository.objects:
        return NOT_EXISTS
    subscription_repository.delete_subscription(subscription)
    return DELETED


# sending errors
@api_router.get("/sending_errors", response_model=List[SendingError])
async def get_all_sending_errors():
    return sending_error_repository.get_all_objects()

#
# # messages
# @api_router.post("/message", response_model=Message)
# async def post_message(message: Message):
#     await message_queue.put(message)
#     return message
