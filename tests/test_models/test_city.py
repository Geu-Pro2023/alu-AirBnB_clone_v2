#!/usr/bin/python3
<<<<<<< HEAD
""" """
from models.state import State
from tests.test_models.test_base_model import TestBaseModel
from models.city import City
=======
"""Unit tests for City class"""
>>>>>>> cdb985bf1439ce5eb65b582b4c93fc576612c422

from models.state import State
from tests.test_models.test_base_model import TestBaseModel
from models.city import City

class TestCity(TestBaseModel):
<<<<<<< HEAD
    """ """
=======
    """Test City class"""
>>>>>>> cdb985bf1439ce5eb65b582b4c93fc576612c422

    def __init__(self, *args, **kwargs):
        """Initialize TestCity instance"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

<<<<<<< HEAD
    def test_state_id(self):
        """ """
        state = State()
        new = self.value()
        new.state_id = state.id
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        new.name = "Batch"
        self.assertEqual(type(new.name), str)
=======
    def test_state_id_attribute(self):
        """Test setting the state_id attribute of City"""
        state = State()
        new_city = self.value()
        new_city.state_id = state.id
        self.assertEqual(type(new_city.state_id), str)

    def test_name_attribute(self):
        """Test setting the name attribute of City"""
        new_city = self.value()
        new_city.name = "Batch"
        self.assertEqual(type(new_city.name), str)

if __name__ == '__main__':
    unittest.main()
>>>>>>> cdb985bf1439ce5eb65b582b4c93fc576612c422
