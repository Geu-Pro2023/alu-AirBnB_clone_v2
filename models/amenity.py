#!/usr/bin/python3
""" State Module for HBNB project """
<<<<<<< HEAD
import os
=======
from os import getenv
>>>>>>> cdb985bf1439ce5eb65b582b4c93fc576612c422

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
<<<<<<< HEAD
    """Amenities of a place"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
=======
    '''amenity class'''
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
>>>>>>> cdb985bf1439ce5eb65b582b4c93fc576612c422
        place_amenities = relationship('Place', secondary="place_amenity")
