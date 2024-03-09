#!/usr/bin/python3
"""Test cases for User class"""

from tests.test_models.test_base_model import TestBaseModel
from models.user import User

class TestUser(TestBaseModel):
    """Test cases for the User class"""

    def __init__(self, *args, **kwargs):
        """Initialize test case"""
        super().__init__(*args, **kwargs)
        self.class_name = "User"
        self.instance = User()

    def test_first_name(self):
        """Test first_name attribute"""
        self.assertIsInstance(self.instance.first_name, str)

    def test_last_name(self):
        """Test last_name attribute"""
        self.assertIsInstance(self.instance.last_name, str)

    def test_email(self):
        """Test email attribute"""
        self.assertIsInstance(self.instance.email, str)

    def test_password(self):
        """Test password attribute"""
        self.assertIsInstance(self.instance.password, str)
