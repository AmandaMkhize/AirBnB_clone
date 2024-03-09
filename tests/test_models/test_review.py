#!/usr/bin/python3
"""Test cases for Review class"""

from tests.test_models.test_base_model import TestBaseModel
from models.review import Review

class TestReview(TestBaseModel):
    """Test cases for the Review class"""

    def __init__(self, *args, **kwargs):
        """Initialize test case"""
        super().__init__(*args, **kwargs)
        self.class_name = "Review"
        self.instance = Review()

    def test_place_id(self):
        """Test place_id attribute"""
        self.assertIsInstance(self.instance.place_id, str)

    def test_user_id(self):
        """Test user_id attribute"""
        self.assertIsInstance(self.instance.user_id, str)

    def test_text(self):
        """Test text attribute"""
        self.assertIsInstance(self.instance.text, str)
