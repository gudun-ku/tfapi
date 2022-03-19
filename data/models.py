from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from data.database import Base


class DbSubscribers(Base):
    __tablename__ = "subscribers"
    id = Column(Integer, primary_key=True, index=True)
    tgname = Column(String)
    email = Column(String)
    topics = relationship("DbTopics", back_populates="subscribers")
    sent = relationship("DbMessages", back_populates="userfrom")
    received = relationship("DbMessages", back_populates="userfrom")


class DbTopics(Base):
    __tablename__ = "topics"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    subscribers = relationship("DbTopics", back_populates="topics")
    messages = relationship("DbMessages")


class DbMessages(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    topic = relationship("DbTopics")
    userfrom = relationship("DbSubscribers",  back_populates="sent")
    userto = relationship("DbSubscribers",  back_populates="received")
