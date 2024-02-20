#!/usr/bin/python3
"""A chatroom database script"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from models.messages import Messages
from sqlalchemy.orm import relationship, mapped_column

class ChatRoom(BaseModel, Base):
    """A chatroom representation"""
    __tablename__= "chatroom"
    last_message = Column(String(128), nullable=True)
    userid1 = Column(String(60), ForeignKey('user.id'))
    userid2 = Column(String(60), ForeignKey('user.id'))

    usr1 = relationship("User", foreign_keys=[userid1])
    usr2 = relationship("User", foreign_keys=[userid2])
    def __init__(self, *args, **kwargs):
        """initializes chatroom"""
        super().__init__(*args, **kwargs)