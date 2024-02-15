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
from web import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    from models import storage
    user = storage.get(User, user_id)
    return user

class User(BaseModel, Base, UserMixin):
    """Representation of a user"""

    __tablename__ = 'user'
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    username = Column(String(128), nullable=False, unique=True)
    email = Column(String(128), nullable=False, unique=True)
    phonenumber = Column(String(20), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    country = Column(String(128), nullable=True)
    region = Column(String(128), nullable=True)
    zone = Column(String(128), nullable=True)
    wereda = Column(String(128), nullable=True)
    idnumb = Column(String(128), nullable=True)
    profilepic = Column(String(128), nullable=True)
    isactive = Column(Boolean, unique=False, default=False)
    properties = relationship("Property", backref="user")

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
