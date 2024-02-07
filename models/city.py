#!/usr/bin/python3
"""A citys database script"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """A city representation"""
    __tablename__ = "city"
    city = Column(String(128), nullable=False)
    subcity = relationship("SubCity",
                              backref="city",
                              cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)