#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
<<<<<<< HEAD
from models import storage_t
=======
>>>>>>> cdb985bf1439ce5eb65b582b4c93fc576612c422
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
<<<<<<< HEAD
    if storage_t == "db":
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship('Place', backref='user')
        reviews = relationship('Review', backref='user')
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
=======
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
>>>>>>> cdb985bf1439ce5eb65b582b4c93fc576612c422
