#!/usr/bin/python3
"""A messages database script"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship, mapped_column

class Messages(BaseModel, Base):
    """A messages representation"""
    __tablename__ = "messages"
    massage = Column(String(1000), nullable=False)
    read = Column(Boolean, unique=False, default=False)
    delivered = Column(Boolean, unique=False, default=False)
    senttoid = mapped_column(String(60), ForeignKey('user.id'))
    sentfromid = mapped_column(String(60), ForeignKey('user.id'))
    chatroomid = mapped_column(String(60), ForeignKey("chatroom.id"))

    sentfrom = relationship("User", foreign_keys=[sentfromid])
    sentto = relationship("User", foreign_keys=[senttoid])
    def __init__(self, *args, **kwargs):
        """initializes messages"""
        super().__init__(*args, **kwargs)