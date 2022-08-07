#!/usr/bin/python3
"""Review module"""

from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Review"""

    def __init__(self, *args, **kwargs):
        """Initialize"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Place id"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """User id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Txt"""
        new = self.value()
        self.assertEqual(type(new.text), str)
