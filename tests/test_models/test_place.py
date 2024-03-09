#!/usr/bin/python3
"""Test cases for Place class"""

from tests.test_models.test_base_model import TestBaseModel
from models.place import Place

class TestPlace(TestBaseModel):
    """Test cases for the Place class"""

    def __init__(self, *args, **kwargs):
        """Initialize test case"""
        super().__init__(*args, **kwargs)
        self.class_name = "Place"
        self.instance = Place()

    def test_city_id(self):
        """Test city_id attribute"""
        self.assertIsInstance(self.instance.city_id, str)

    def test_user_id(self):
        """Test user_id attribute"""
        self.assertIsInstance(self.instance.user_id, str)

    def test_name(self):
        """Test name attribute"""
        self.assertIsInstance(self.instance.name, str)

    def test_description(self):
        """Test description attribute"""
        self.assertIsInstance(self.instance.description, str)

    def test_number_rooms(self):
        """Test number_rooms attribute"""
        self.assertIsInstance(self.instance.number_rooms, int)

    def test_number_bathrooms(self):
        """Test number_bathrooms attribute"""
        self.assertIsInstance(self.instance.number_bathrooms, int)

    def test_max_guest(self):
        """Test max_guest attribute"""
        self.assertIsInstance(self.instance.max_guest, int)

    def test_price_by_night(self):
        """Test price_by_night attribute"""
        self.assertIsInstance(self.instance.price_by_night, int)

    def test_latitude(self):
        """Test latitude attribute"""
        self.assertIsInstance(self.instance.latitude, float)

    def test_longitude(self):
        """Test longitude attribute"""
        self.assertIsInstance(self.instance.longitude, float)

    def test_amenity_ids(self):
        """Test amenity_ids attribute"""
        self.assertIsInstance(self.instance.amenity_ids, list)
