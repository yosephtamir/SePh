#!/usr/bin/python3
"""A subcitys database script"""
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class SubCity(BaseModel, Base):
    """A subcity representation"""
    __tablename__ = "subcity"
    subcity = Column(String(128), nullable=False)
    cityid = Column(String(60), ForeignKey("city.id"), nullable=False)
    Place = relationship("Place",
                            backref="subcity",
                            cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        """initializes subcity"""
        super().__init__(*args, **kwargs)