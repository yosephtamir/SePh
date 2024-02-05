#!/usr/bin/python3
"""A places database script"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey

class Place(BaseModel, Base):
    """A place representation"""
    __tablename__ = "place"
    city = Column(String(128), nullable=False)
    subcity = Column(String(128), nullable=False)
    addressLine1 = Column(String(1000), nullable=False)
    addressLine2 = Column(String(1000), nullable=True)
    

    def __init__(self, *args, **kwargs):
        """initializes place"""
        super().__init__(*args, **kwargs)