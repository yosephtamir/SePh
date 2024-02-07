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
    userid = mapped_column(String(60), ForeignKey('user.id'))

    def __init__(self, *args, **kwargs):
        """initializes chatroom"""
        super().__init__(*args, **kwargs)