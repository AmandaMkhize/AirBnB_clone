#!/usr/bin/python3
"""Test cases for State class"""

from tests.test_models.test_base_model import TestBaseModel
from models.state import State

class TestState(TestBaseModel):
    """Test cases for the State class"""

    def __init__(self, *args, **kwargs):
        """Initialize test case"""
        super().__init__(*args, **kwargs)
        self.class_name = "State"
        self.instance = State()

    def test_name(self):
        """Test name attribute"""
        self.assertIsInstance(self.instance.name, str)
