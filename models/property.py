#!/usr/bin/python3
"""A propertys database script"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Property(BaseModel, Base):
    """A property representation"""
    __tablename__ = "property"
    name = Column(String(128), nullable=False)
    price = Column(String(128), nullable=False)
    details = Column(String(1000), nullable=False)
    addressLine2 = Column(String(1000), nullable=True)
    user_id = Column(String(60), ForeignKey('user.id'), nullable=False)
    place_id = Column(String(60), ForeignKey('place.id'), nullable=False)
    images = relationship("PropertyImage", backref=property)
    

    def __init__(self, *args, **kwargs):
        """initializes property"""
        super().__init__(*args, **kwargs)