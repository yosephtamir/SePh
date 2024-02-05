#!/usr/bin/python3
"""A propertyimages database script"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey


class PropertyImage(BaseModel, Base):
    """A propertyimage representation"""
    __tablename__ = "propertyimage"
    name = Column(String(128), nullable=False)
    property_id = Column(String(60), ForeignKey('property.id'), nullable=False)
    

    def __init__(self, *args, **kwargs):
        """initializes propertyimage"""
        super().__init__(*args, **kwargs)