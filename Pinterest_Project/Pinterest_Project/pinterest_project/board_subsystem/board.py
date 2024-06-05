"""
This module has the specific definition of the Board class.

Autor: Edison David Álvarez <edalvarezv@udistrital.edu.co>
"""

from .pin import Pin


class Board:
    """
    This class represents a board, which is a collection of pins or
    images, therefore, it is made up of objects of the pin class.
    """

    def __init__(self, id_board: int, name: str, description: str):
        self.id_board = id_board
        self.name = name
        self.description = description
        self.__pin_list = []

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

    def get_all_pins(self):
        """
        This method is responsible for obtaining all the pins of a board

        Returns:
            List[Pin]: The list of all pins.
        """
        return self.__pin_list
