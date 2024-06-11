"""
This module has a unique implementation of a catalog that includes the
addition of its timing and memory performance decorators.

Authors: Edison David Alvarez <edalvarezv@udistrital.edu.co>
         Juan Diego Lozada <juandiegolozada123@gmail.com>
"""

from typing import List
from ..catalog_subsystem import Catalog, TimeDecorator, MemoryDecorator
from ..board_subsystem import Board, Pin


class CatalogProxy:
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
            List[Board]: A list of all boards in the catalog.
        """
        return self.__catalog.get_all_boards()

    def add_board(self, id_board: int, user_id: int, name: str, description: str):
        """
        This method adds a new board to the catalog.

        Args:
            id_board (int): The ID of the board.
            user_id (int): The ID of the user.
            name (str): The name of the board.
            description (str): A description of the board.
        """
        board = Board(id_board, user_id, name, description)
        self.__catalog.add_board(board)

    def delete_board(self, board_id):
        """
        This method deletes a board from the catalog by its ID.

        Args:
            board_id (int): The ID of the board to delete.
        """
        for board in self.__catalog.get_all_boards():
            if board.board_id == board_id:
                self.__catalog.delete_board(board)

    def get_all_pins(self) -> List[Pin]:
        """
        This method retrieves all pins from the catalog.

        Returns:
            List[Pin]: A list of all pins in the catalog.
        """
        return self.__catalog.get_all_pins()

    def add_pin(self, id_board: int, id_pin: str, user_id: int,
                name: str, description: str, url: str):
        """
        This method adds a new pin to a specified board in the catalog.

        Args:
            id_board (int): The ID of the board to add the pin to.
            id_pin (str): The ID of the pin.
            user_id (int): The ID of the user.
            name (str): The name of the pin.
            description (str): A description of the pin.
            url (str): The URL associated with the pin.
        """
        pin = Pin(id_pin, user_id, name, description, url)
        for board in self.__catalog.get_all_boards():
            if board.id_board == id_board:
                self.__catalog.add_pin(board, pin)

    def delete_pin(self, id_pin):
        """
        This method deletes a pin from the catalog by its ID.

        Args:
            id_pin (str): The ID of the pin to delete.
        """
        for board in self.__catalog.get_all_boards():
            for pins in board.get_all_pins():
                if pins.id_pin == id_pin:
                    self.__catalog.delete_pin(pins)

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
        return self.__catalog.get_pins_by_category(category)
