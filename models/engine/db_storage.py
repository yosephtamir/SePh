#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from models.category import Category
from models.chatroom import ChatRoom
from models.messages import Messages
from models.place import Place
from models.property import Property
from models.propertyimage import PropertyImage
from models.roomusers import RoomUser
from models.user import User
from models.subcity import SubCity
from models.city import City
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Category": Category, "ChatRoom": ChatRoom,
           "Place": Place, "Messages": Messages, "Property": Property,
           "PropertyImage": PropertyImage, "RoomUser": RoomUser, "User": User,
           "SubCity": SubCity, "City": City}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine("sqlite:///test.db", echo=True)
    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)
    

    def valCheck(self, checkedVal, value, cls="User"):
        """Used as a validation checker"""
        if checkedVal == "username":
            objs = self.__session.query(classes[cls]).filter_by(username=value).first()
            return objs
        
        if checkedVal == "email":
            objs = self.__session.query(classes[cls]).filter_by(email=value).first()
            return objs
        
        if checkedVal == "phonenumber":
            objs = self.__session.query(classes[cls]).filter_by(phonenumber=value).first()
            return objs
        
        if checkedVal == "name":
            objs = self.__session.query(classes[cls]).filter_by(name=value).first()
            return objs

        if checkedVal == "id":
            objs = self.__session.query(classes[cls]).filter_by(id=value).first()
            return objs

    
    def countablefetch(self, cls=None, num=3):
        """query on the current database session with limit"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).limit(num).all()

                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count