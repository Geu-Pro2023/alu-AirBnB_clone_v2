#!/usr/bin/python3
<<<<<<< HEAD
import unittest
import models
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.city import City
import os


# skip these tests if db is not the storage
@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "skip if not fs")
class TestDBSorage(unittest.TestCase):
    """test DB Storage"""

    def setUp(self):
        """set up the test environment"""
        self.storage = models.storage

    def tearDown(self):
        """Remove storage file at the end of tests"""
        del self.storage

    def test_user(self):
        """Tests the user"""
        user = User(name="Brian", email="brian@gmail.com", password="Brian123")
        user.save()
        self.assertFalse(user.id in self.storage.all())
        self.assertEqual(user.name, "Brian")

    def test_city(self):
        """ Tests the city """
        state = State(name="Kenya")
        state.save()
        city = City(name="Nairobi")
        city.state_id = state.id
        city.save()
        self.assertFalse(city.id in self.storage.all())
        self.assertEqual(city.name, "Nairobi")

    def test_state(self):
        """Test state"""
        state = State(name="Kenya")
        state.save()
        self.assertFalse(state.id in self.storage.all())
        self.assertEqual(state.name, "Kenya")

    def test_place(self):
        """ Test the place"""
        state = State(name="Kenya")
        state.save()

        city = City(name="Nairobi")
        city.state_id = state.id
        city.save()

        user = User(name="Brian", email="brian@gmail.com", password="Brian123")
        user.save()

        place = Place(name="PentHouse", number_rooms=4)
        place.city_id = city.id
        place.user_id = user.id
        place.save()

        self.assertFalse(place.id in self.storage.all())
        self.assertEqual(place.number_rooms, 4)
        self.assertEqual(place.name, "PentHouse")

    def test_amenity(self):
        """tests the amenity"""
        amenity = Amenity(name="Spoon")
        amenity.save()
        self.assertFalse(amenity.id in self.storage.all())
        self.assertEqual(amenity.name, "Spoon")

    def test_review(self):
        """Tests the review"""
        state = State(name="Kenya")
        state.save()

        city = City(name="Nairobi")
        city.state_id = state.id
        city.save()

        user = User(name="Brian", email="brian@gmail.com", password="Brian123")
        user.save()

        place = Place(name="PentHouse", number_rooms="4")
        place.city_id = city.id
        place.user_id = user.id
        place.save()

        review = Review(text="work smart", place_id=place.id, user_id=user.id)
        review.save()

        self.assertFalse(review.id in self.storage.all())
        self.assertEqual(review.text, "work smart")


    if __name__ == '__main__':
        unittest.main()
=======
"""Defines the DBStorage engine."""
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """Represents a database storage engine.

    Attributes:
        __engine (sqlalchemy.Engine): The working SQLAlchemy engine.
        __session (sqlalchemy.Session): The working SQLAlchemy session.
    """

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
        """Query on the curret database session all objects of the given class.

        If cls is None, queries all types of objects.

        Return:
            Dict of queried classes in the format <class name>.<obj id> = obj.
        """
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """Add obj to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the working SQLAlchemy session."""
        self.__session.close()
>>>>>>> cdb985bf1439ce5eb65b582b4c93fc576612c422
