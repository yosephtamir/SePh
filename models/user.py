#!/usr/bin/python3
""" A Users database class"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from models.property import Property
from models.messages import Messages
from sqlalchemy import Column, String, Numeric
from sqlalchemy.orm import relationship
from hashlib import md5


class User(BaseModel, Base):
    """Representation of a user"""

    __tablename__ = 'user'
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    username = Column(String(128), nullable=False, unique=True)
    email = Column(String(128), nullable=False, unique=True)
    phonenumber = Column(Numeric(20), nullable=True)
    password = Column(String(128), nullable=True)
    country = Column(String(128), nullable=True)
    region = Column(String(128), nullable=True)
    zone = Column(String(128), nullable=True)
    wereda = Column(String(128), nullable=True)
    idcard = Column(String(128), nullable=True)
    profilepic = Column(String(128), nullable=True)
    messages = relationship("Messages", backref="user")
    properties = relationship("Property", backref="user")

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)