#!/usr/bin/python3
<<<<<<< HEAD
""" """
from tests.test_models.test_base_model import TestBaseModel
from models.user import User
=======
"""Unit tests for User class"""
>>>>>>> cdb985bf1439ce5eb65b582b4c93fc576612c422

from tests.test_models.test_base_model import TestBaseModel
from models.user import User

class TestUser(TestBaseModel):
<<<<<<< HEAD
    """ Test for user"""
=======
    """Test User class"""
>>>>>>> cdb985bf1439ce5eb65b582b4c93fc576612c422

    def __init__(self, *args, **kwargs):
        """Initialize TestUser instance"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

<<<<<<< HEAD
    def test_first_name(self):
        """ """
        new = self.value()
        new.first_name = "Chyna"
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ """
        new = self.value()
        new.last_name = "Chyna"
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ """
        new = self.value()
        new.email = "angoyewally@gmail.com"
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ """
        new = self.value()
        new.password = "123aashja"
        self.assertEqual(type(new.password), str)
=======
    def test_first_name_attribute(self):
        """Test setting the first_name attribute of User"""
        new_user = self.value()
        new_user.first_name = "Chyna"
        self.assertEqual(type(new_user.first_name), str)

    def test_last_name_attribute(self):
        """Test setting the last_name attribute of User"""
        new_user = self.value()
        new_user.last_name = "Chyna"
        self.assertEqual(type(new_user.last_name), str)

    def test_email_attribute(self):
        """Test setting the email attribute of User"""
        new_user = self.value()
        new_user.email = "angoyewally@gmail.com"
        self.assertEqual(type(new_user.email), str)

    def test_password_attribute(self):
        """Test setting the password attribute of User"""
        new_user = self.value()
        new_user.password = "123aashja"
        self.assertEqual(type(new_user.password), str)

if __name__ == '__main__':
    unittest.main()
>>>>>>> cdb985bf1439ce5eb65b582b4c93fc576612c422
