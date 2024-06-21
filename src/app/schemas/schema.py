import datetime
from typing import Union, Dict, List, Optional

from pydantic import BaseModel


class Message(BaseModel):
    subject_name: str
    data: Union[Dict, List]


class Subject(BaseModel):
    name: str
    description: Optional[str]


class Subscription(BaseModel):
    url: str
    subject_name: str


class SendingError(BaseModel):
    subscription: Subscription
    message: Message
    description: str
    time: datetime.datetime

