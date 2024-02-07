#!/usr/bin/python3
"""A places database script"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey

class Place(BaseModel, Base):
    """A place representation"""
    __tablename__ = "place"
    addressLine1 = Column(String(1000), nullable=False)
    addressLine2 = Column(String(1000), nullable=True)
    userid = Column(String(60), ForeignKey('user.id'), nullable=False)
    subcityid = Column(String(60), ForeignKey('subcity.id'), nullable=False)
    

    def __init__(self, *args, **kwargs):
        """initializes place"""
        super().__init__(*args, **kwargs)