#!/usr/bin/python3
<<<<<<< HEAD
""" """
=======
"""Unit tests for Amenity class"""

import unittest
>>>>>>> cdb985bf1439ce5eb65b582b4c93fc576612c422
from tests.test_models.test_base_model import TestBaseModel
from models.amenity import Amenity


<<<<<<< HEAD
class test_Amenity(TestBaseModel):
    """ """
=======
class TestAmenity(TestBaseModel):
    """Test Amenity class"""
>>>>>>> cdb985bf1439ce5eb65b582b4c93fc576612c422

    def __init__(self, *args, **kwargs):
        """Initialize Amenity test instance"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

<<<<<<< HEAD
    def test_name2(self):
        """ """
        new = self.value()
        new.name = "amenity"
        self.assertEqual(type(new.name), str)
=======
    def test_name(self):
        """Test the 'name' attribute of Amenity"""
        new_amenity = self.value()
        new_amenity.name = "amenity"
        self.assertEqual(type(new_amenity.name), str)


if __name__ == '__main__':
    unittest.main()
>>>>>>> cdb985bf1439ce5eb65b582b4c93fc576612c422
