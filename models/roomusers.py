#!/usr/bin/python3
"""A roomusers database script"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class RoomUser(BaseModel, Base):
    """A roomuser representation"""
    __tablename__ = "roomuser"
    name = Column(String(128), nullable=False)
    user_id = Column(String(60), ForeignKey('user.id'), nullable=False)
    place_id = Column(String(60), ForeignKey('place.id'), nullable=False)

    

    def __init__(self, *args, **kwargs):
        """initializes roomuser"""
        super().__init__(*args, **kwargs)