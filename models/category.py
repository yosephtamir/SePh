#!/usr/bin/python3
"""A category represantation script"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String

class Category(BaseModel, Base):
    """Representation of Category """
    __tablename__ = 'category'
    name = Column(String(128), unique=True,nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes category"""
        super().__init__(*args, **kwargs)