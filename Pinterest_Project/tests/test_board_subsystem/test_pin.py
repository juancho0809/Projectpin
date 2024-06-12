"""
This file has some test cases related to Pin class.

Authors: Edison David Alvarez <edalvarezv@udistrital.edu.co>
         Juan Diego Lozada <juandiegolozada123@gmail.com>
"""

import pytest
from pinterest_project.board_subsystem import Pin

class TestPin:
    """This class tests the Pin class"""

    @classmethod
    def setup_class(cls):
        """This is a method to create dummy data for Pin creation"""
        cls.data_test = {
            "id_pin": 123,
            "user_id": 42,
            "name": "Sample Pin",
            "description": "This is a sample pin for testing purposes.",
            "url": "http://example.com/sample-pin"
        }

    def test_create_pin(self):
        """This is a test case to verify the creation of a Pin object"""
        new_pin = Pin(
            id_pin=self.data_test["id_pin"],
            user_id=self.data_test["user_id"],
            name=self.data_test["name"],
            description=self.data_test["description"],
            url=self.data_test["url"],
        )
        assert new_pin.id_pin == self.data_test["id_pin"]
        assert new_pin.user_id == self.data_test["user_id"]
        assert new_pin.name == self.data_test["name"]
        assert new_pin.description == self.data_test["description"]
        assert new_pin.url == self.data_test["url"]

    def test_add_category_pin(self):
        """This is a test case to verify adding a new category to a Pin object"""
        new_pin = Pin(
            id_pin=self.data_test["id_pin"],
            user_id=self.data_test["user_id"],
            name=self.data_test["name"],
            description=self.data_test["description"],
            url=self.data_test["url"],
        )
        new_pin.add_category_pin("nature")
        assert "nature" in new_pin.categories

    def test_remove_category_pin(self):
        """This is a test case to verify removing a category from a Pin object"""
        new_pin = Pin(
            id_pin=self.data_test["id_pin"],
            user_id=self.data_test["user_id"],
            name=self.data_test["name"],
            description=self.data_test["description"],
            url=self.data_test["url"],
        )
        new_pin.add_category_pin("nature")
        assert "nature" in new_pin.categories
        new_pin.remove_category_pin("nature")
        assert "nature" not in new_pin.categories
