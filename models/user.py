#!/usr/bin/python3
""" A Users database class"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from models.property import Property
from models.messages import Messages
from sqlalchemy import Column, String, Numeric, Boolean
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Representation of a user"""

    __tablename__ = 'user'
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    username = Column(String(128), nullable=False, unique=True)
    email = Column(String(128), nullable=False, unique=True)
    phonenumber = Column(String(20), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    country = Column(String(128), nullable=False)
    region = Column(String(128), nullable=False)
    zone = Column(String(128), nullable=False)
    wereda = Column(String(128), nullable=False)
    idnumb = Column(String(128), nullable=False)
    profilepic = Column(String(128), nullable=True)
    isactive = Column(Boolean, unique=False, default=False)
    properties = relationship("Property", backref="user")

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
