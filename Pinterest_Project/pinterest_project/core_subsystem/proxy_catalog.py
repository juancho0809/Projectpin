"""
This module has a unique implementation of a catalog that includes the
addition of its timing and memory performance decorators.

Authors: Edison David Alvarez <edalvarezv@udistrital.edu.co>
         Juan Diego Lozada <juandiegolozada123@gmail.com>
"""

from typing import List
from ..catalog_subsystem import Catalog, CatalogInterface, TimeDecorator, MemoryDecorator
from ..board_subsystem import Board, Pin


class CatalogProxy(CatalogInterface):
    """This class is a proxy for the catalog class."""

    _instance_catalog = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance_catalog:
            cls._instance = super(CatalogProxy, cls).__new__(cls, *args, **kwargs)
        return cls._instance_catalog

    def __init__(self):
        self.__catalog = Catalog()
        self.__catalog = TimeDecorator(self.__catalog)
        self.__catalog = MemoryDecorator(self.__catalog)

    def get_all_boards(self) -> List[Board]:
        """
        This method retrieves all boards from the catalog.

        Returns:
            list[Board]: A list of all boards in the catalog.
        """
        return self.__catalog.get_all_boards()

    def add_board(self, board: Board):
        """
        This method adds a new board to the catalog.

        Args:
            board (Board): The board object to be added to the catalog.
        """
        return self.__catalog.add_board(board)

    def delete_board(self, board: Board):
        """
        This method deletes a board from the catalog.

        Args:
            board (Board): The board object to be deleted from the catalog.
        """
        return self.__catalog.delete_board(board)

    def get_all_pins(self) -> List[Pin]:
        """
        This method recovers all the pines from the catalgo boards.

        Returns:
            list[Pin]: A list of all pines in the catalog.
        """
        return self.__catalog.get_all_pins()

    def add_pin(self, board: Board, pin: Pin):
        """
        This method adds a new pin to a specific board in the catalog.

        Args:
            board (Board): The board to which the pin will be added.
            pin (Pin): The pin object to be added to the board.
        """
        return self.__catalog.add_pin(board, pin)

    def delete_pin(self, pin: Pin):
        """
        This method deletes a pin from a specific board in the catalog.

        Args:
            board (Board): The board from which the pin will be removed.
            pin (Pin): The pin object to be removed from the board.
        """
        return self.__catalog.delete_pin(pin)

    def get_board_by_name(self, name: str) -> Board:
        """
        This method retrieves a board by its name.

        Args:
            name (str): The name of the board to retrieve.

        Returns:
            Board: The board with the specified name, or None if not found.
        """
        return self.__catalog.get_board_by_name(name)

    def get_boards_by_category(self, category: str)  -> List[Board]:
        """
        This method retrieves all boards in a specific category from the catalog.

        Args:
            category (str): The category to filter the boards by.

        Returns:
            list[Board]: A list of boards that belong to the specified category.
        """
        return self.__catalog.get_boards_by_category(category)

    def get_pin_by_name(self, name: str) -> Pin:
        """
        This method retrieves a pin by its name from all boards in the catalog.

        Args:
            name (str): The name of the pin to retrieve.

        Returns:
            Pin: The pin with the specified name, or None if not found.
        """
        return self.__catalog.get_pin_by_name(name)

    def get_pins_by_category(self, category: str) -> List[Pin]:
        """
        This method retrieves all pins in a specific category from the catalog.

        Args:
            category (str): The category to filter the pins by.

        Returns:
            list[Pin]: A list of pins that belong to the specified category.
        """
        return self.__catalog.get_boards_by_category(category)
