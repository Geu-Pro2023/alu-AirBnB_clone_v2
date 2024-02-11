#!/usr/bin/python3

"""db_storage.py use database"""

<<<<<<< HEAD
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """ create tables in environmental"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize a new DBStorage instance."""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ """
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for ele in query:
                key = "{}.{}".format(type(ele).__name__, ele.id)
                dic[key] = ele
        else:
            lists = [State, City, User, Place, Review, Amenity]
            for classe in lists:
                query = self.__session.query(classe)
                for ele in query:
                    key = "{}.{}".format(type(ele).__name__, ele.id)
                    dic[key] = ele

        return (dic)

    def new(self, obj):
        """Add obj to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session."""
        Base.metadata.create_all(self.__engine)
        ses = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(ses)
        self.__session = Session()

    def close(self):
        """Close the working SQLAlchemy session."""
=======
import os

import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """Represents database storage"""
    __engine = None
    __session = None

    """
    To set the environment variables, depending on your operating system:
    export MY_VARIABLE=<MY_VARIABLE_VALUE>  (Linux)
    set MY_VARIABLE=<MY_VARIABLE_VALUE>  (Windows)
    """

    def __init__(self):
        """Initialize object"""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')

        self.__engine = sqlalchemy.create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'
            .format(user,
                    password,
                    host,
                    database), pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == "test":
            # from models.base_model import Base
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Gets all objects depending on the class name"""
        # from models.base_model import BaseModel
        # from models.user import User
        # from models.place import Place
        # from models.state import State
        # from models.city import City
        # from models.amenity import Amenity
        # from models.review import Review

        classes = {
            'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        obj_dict = {}
        if cls is not None and cls in classes:
            class_objects = self.__session.query(classes[cls]).all()
            for obj in class_objects:
                key = obj.__class__.__name__ + "." + obj.id
                obj_dict[key] = obj

        if cls is None:
            for cls in classes:
                class_objects = self.__session.query(classes[cls]).all()
                for obj in class_objects:
                    key = obj.__class__.__name__ + "." + obj.id
                    obj_dict[key] = obj

        return obj_dict

    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        session = scoped_session(session_factory)
        self.__session = session()

    def close(self):
        """Close the session"""
>>>>>>> cdb985bf1439ce5eb65b582b4c93fc576612c422
        self.__session.close()
