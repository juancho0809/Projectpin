"""
This module has the interface of the Board class.

Author: Edison David Álvarez <edalvarezv@udistrital.edu.co>
"""

from abc import ABC, abstractmethod
from typing import List
from .pin import Pin

class BoardInterface(ABC):
    """
    This class represents a board, which is a collection of pins or
    images, therefore, it is made up of objects of the pin class.
    """
    @abstractmethod
    def add_pin(self, pin: Pin):
        """
        This method is responsible for adding a pin object from the pin_list
        Args:
            pin (Pin): An object of class pin
        """

    @abstractmethod
    def delete_pin(self, pin: Pin):
        """
        This method is responsible for removing a pin object from the pin_list.
        Args:
            pin (Pin): An object of class pin
        """
    @abstractmethod
    def get_all_pins(self) -> List[Pin]:
        """
        This method is responsible for obtaining all the pins of a board

        Returns:
            List[Pin]: The list of all pins.
        """

    @abstractmethod
    def get_pin_by_name(self, name: str) -> Pin:
        """
        This method retrieves a pin by name from the board

        Arguments:
            name (string): The name of the pin to retrieve.

        Returns:
            Pin: The pin with the specified name, or None if not found.
        """

    @abstractmethod
    def get_pins_by_category(self, category: str) -> List[Pin] :
        """
        This method retrieves all pins from a specific category on a board.

        Arguments:
            category (string): The category to filter pins by.

        Returns:
            list[Pin]: A list of pins that belong to the specified category.
        """

    @abstractmethod
    def add_category_board(self, category: str):
        """
        This method adds a new category to the Board
        
        Arguments:
            category (string): the category to add
        """

    @abstractmethod
    def remove_category_board(self, category: str):
        """
        This method removes a category from the board
        
        Arguments:
            category (string): the category to delete
        """
