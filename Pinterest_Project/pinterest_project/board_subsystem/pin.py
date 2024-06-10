"""
This file has the specific definition of the Pin class

Authors: Edison David Alvarez <edalvarezv@udistrital.edu.co>
         Juan Diego Lozada <juandiegolozada123@gmail.com>
"""

class Pin:
    """This class represents a Pin object, which can be thought of as an image"""

    def __init__(
        self, id_pin: str, user_id: int, name: str, description: str, url: str):
        self.id_pin = id_pin
        self.user_id = user_id
        self.name = name
        self.description = description
        self.url = url
        self.categories = []

    def modify_pin(self):
        """This method is responsible for modifying an existing pin"""

    def add_category_pin(self, category: str):
        """
        This method adds a new category to the pin
        
        Arguments:
            category (string): the category to add
        """
        category_lower = category.lower()
        if category_lower not in self.categories:
            self.categories.append(category)

    def remove_category_pin(self, category: str):
        """
        This method removes a category from the pin
        
        Arguments:
            category (string): the category to delete
        """
        category_lower = category.lower()
        if category_lower in self.categories:
            self.categories.remove(category)
