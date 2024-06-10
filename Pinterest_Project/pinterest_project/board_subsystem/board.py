"""
This module has the specific definition of the Board class.

Autor: Edison David Álvarez <edalvarezv@udistrital.edu.co>
"""
from typing import List
from .pin import Pin
from .board_interface import BoardInterface

class Board(BoardInterface):
    """
    This class represents a board, which is a collection of pins or
    images, therefore, it is made up of objects of the pin class.
    """

    def __init__(self, id_board: int, user_id: int, name: str, description: str):
        self.id_board = id_board
        self.user_id = user_id
        self.name = name
        self.description = description
        self.__pin_list = []
        self.categories = []

    def add_pin(self, pin: Pin):
        """
        This method is responsible for adding a pin object from the pin_list
        Args:
            pin (Pin): An object of class pin
        """
        self.__pin_list.append(pin)

    def delete_pin(self, pin: Pin):
        """
        This method is responsible for removing a pin object from the pin_list.
        Args:
            pin (Pin): An object of class pin
        """
        self.__pin_list.remove(pin)

    def get_all_pins(self) -> List[Pin]:
        """
        This method is responsible for obtaining all the pins of a board

        Returns:
            List[Pin]: The list of all pins.
        """
        return self.__pin_list

    def get_pin_by_name(self, name: str) -> Pin:
        """
        This method retrieves a pin by name from the board

        Arguments:
            name (string): The name of the pin to retrieve.

        Returns:
            Pin: The pin with the specified name, or None if not found.
        """
        for pin in self.__pin_list:
            if pin.name == name:
                return pin
        return None

    def get_pins_by_category(self, category: str) -> List[Pin]:
        """
        This method retrieves all pins from a specific category on a board.

        Arguments:
            category (string): The category to filter pins by.

        Returns:
            list[Pin]: A list of pins that belong to the specified category.
        """
        pins_in_category = []
        for pin in self.__pin_list:
            for categories in pin.categories:
                if categories == category:
                    pins_in_category.append(pin)
        return pins_in_category

    def add_category_board(self, category: str):
        """
        This method adds a new category to the board
        
        Arguments:
            category (string): the category to add
        """
        category_lower = category.lower()
        if category_lower not in self.categories:
            self.categories.append(category)

    def remove_category_board(self, category: str):
        """
        This method removes a category from the board
        
        Arguments:
            category (string): the category to delete
        """
        category_lower = category.lower()
        if category_lower in self.categories:
            self.categories.remove(category)
