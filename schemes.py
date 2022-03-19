from zipfile import _ClosableZipStream
from pydantic import BaseModel
from typing import List


class SubscriberBase(BaseModel):
    tgname: str
    email: str


class SubscriberPopulate(BaseModel):
    id: int
    tgname: str

    class Config():
        orm_mode = True


class TopicBase(BaseModel):
    name: str


class TopicPopulate(BaseModel):
    id: int
    name: str

    class Config():
        orm_mode = True


class MessageBase(BaseModel):
    id: int
    content: str


class MessagePopulate(BaseModel):
    id: int
    content: str

    class Config():
        orm_mode = True


class SubscriberResponse(BaseModel):
    tgname: str
    email: str
    subsciptions: List[TopicPopulate] = []

    class Config():
        orm_mode = True
