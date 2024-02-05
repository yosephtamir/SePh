#!/usr/bin/python3
"""A messages database script"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey

class Messages(BaseModel, Base):
    """A messages representation"""
    __tablename__ = "messages"
    massage = Column(String(1000), nullable=False)
    sentto = Column(String(60), ForeignKey('user.id'), nullable=False)
    sentfrom = Column(String(60), ForeignKey('user.id'), nullable=False)
    chatroomid = Column(String(60), ForeignKey("chatroom.id"), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes messages"""
        super().__init__(*args, **kwargs)