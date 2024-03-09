#!/usr/bin/python3
"""Test cases for City class"""

from tests.test_models.test_base_model import TestBaseModel
from models.city import City

class TestCity(TestBaseModel):
    """Test cases for the City class"""

    def __init__(self, *args, **kwargs):
        """Initialize test case"""
        super().__init__(*args, **kwargs)
        self.class_name = "City"
        self.instance = City()

    def test_state_id(self):
        """Test state_id attribute"""
        self.assertIsInstance(self.instance.state_id, str)

    def test_name(self):
        """Test name attribute"""
        self.assertIsInstance(self.instance.name, str)
