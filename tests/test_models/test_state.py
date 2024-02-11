#!/usr/bin/python3
<<<<<<< HEAD
""" """
=======
"""Unit tests for State class"""

import unittest
>>>>>>> cdb985bf1439ce5eb65b582b4c93fc576612c422
from tests.test_models.test_base_model import TestBaseModel
from models.state import State


class TestState(TestBaseModel):
<<<<<<< HEAD
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "California"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        new.name = "Arizona"
        self.assertEqual(type(new.name), str)
=======
    """Test State class"""

    def test_name_property(self):
        """Test the 'name' property of State"""
        new_state = State()
        new_state.name = "Arizona"
        self.assertEqual(type(new_state.name), str)

if __name__ == '__main__':
    unittest.main()
>>>>>>> cdb985bf1439ce5eb65b582b4c93fc576612c422
