"""
This file has the specific definition of the Pin class

Author: Edison David Alvarez <edalvarezv@udistrital.edu.co>
"""


class Pin:
    """This class represents a Pin object, which can be thought of as an image"""

    def __init__(
        self, id_pin: str, name: str, description: str, url: str, categories: str
    ):
        self.id_pin = id_pin
        self.name = name
        self.description = description
        self.url = url
        self.categories = categories

    def modify_pin(self):
        """This method is responsible for modifying an existing pin"""
