#!/usr/bin/python3
<<<<<<< HEAD
""" """
from models.place import Place
from models.user import User
from tests.test_models.test_base_model import TestBaseModel
from models.review import Review
=======
"""Unit tests for Review class"""
>>>>>>> cdb985bf1439ce5eb65b582b4c93fc576612c422

from models.place import Place
from models.user import User
from tests.test_models.test_base_model import TestBaseModel
from models.review import Review

class TestReview(TestBaseModel):
<<<<<<< HEAD
    """Test for review """
=======
    """Test Review class"""
>>>>>>> cdb985bf1439ce5eb65b582b4c93fc576612c422

    def __init__(self, *args, **kwargs):
        """Initialize TestReview instance"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

<<<<<<< HEAD
    def test_place_id(self):
        """ """
        new = self.value()
        place = Place()
        new.place_id = place.id
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        user = User()
        new.user_id = user.id
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value()
        new.text = ""
        self.assertEqual(type(new.text), str)
=======
    def test_place_id_attribute(self):
        """Test setting the place_id attribute of Review"""
        new_review = self.value()
        place = Place()
        new_review.place_id = place.id
        self.assertEqual(type(new_review.place_id), str)

    def test_user_id_attribute(self):
        """Test setting the user_id attribute of Review"""
        new_review = self.value()
        user = User()
        new_review.user_id = user.id
        self.assertEqual(type(new_review.user_id), str)

    def test_text_attribute(self):
        """Test setting the text attribute of Review"""
        new_review = self.value()
        new_review.text = ""
        self.assertEqual(type(new_review.text), str)

if __name__ == '__main__':
    unittest.main()
>>>>>>> cdb985bf1439ce5eb65b582b4c93fc576612c422
