#!/usr/bin/python3
"""Test cases for Amenity class"""

from tests.test_models.test_base_model import TestBaseModel
from models.amenity import Amenity

class TestAmenity(TestBaseModel):
    """Test cases for the Amenity class"""

    def __init__(self, *args, **kwargs):
        """Initialize test case"""
        super().__init__(*args, **kwargs)
        self.class_name = "Amenity"
        self.instance = Amenity()

    def test_name(self):
        """Test name attribute"""
        self.assertIsInstance(self.instance.name, str)
