"""
This file contains the concrete implementation of catalog, which 
inherits from CatalogInterface

Autor: Edison David Álvarez <edalvarezv@udistrital.edu.co>
"""

from .catalog_interface import CatalogInterface
from ..board_subsystem.board import Board

class Catalog(CatalogInterface):
    """
    This is the specific Catalog class that wound from CatalgoInterface
    """
    __board_list = []

    def __new__(cls):
        """
        This is the private constructor of the Catalog, so that it is 
        a Singelton
        """
        if cls.__board_list is None:
            cls._instance = super().__new__(cls)
            # Data initialization through the database
        return cls.__board_list

    def get_all_boards(self):
        """
        This method retrieves all boards from the catalog.

        Returns:
            list[Board]: A list of all boards in the catalog.
        """
        return self.__board_list

    def add_board(self, board: Board):
        """
        This method adds a new board to the catalog.

        Args:
            board (Board): The board object to be added to the catalog.
        """
        if board not in self.__board_list:
            self.__board_list.append(board)

    def delete_board(self, board: Board):
        """
        This method deletes a board from the catalog.

        Args:
            board (Board): The board object to be deleted from the catalog.
        """
        if board in self.__board_list:
            self.__board_list.remove(board)

    def get_all_pins(self):
        """
        This method recovers all the pines from the catalgo boards.

        Returns:
        list[Pin]: A list of all pines in the catalog.
        """
        pins = []
        for board in self.__board_list:
            pins.extend(board.get_pins())
        return pins

    def get_board_by_category(self, category: str):
        """
        This method  retrieves all boards in a specific category from the catalog.

        Args:
            category (str): The category to filter the boards by.

        Returns:
            list[Board]: A list of boards that belong to the specified category.
        """

    def get_pin_by_category(self, category: str):
        """
        This method retrieves all pins in a specific category from the catalog.

        Args:
            category (str): The category to filter the pins by.

        Returns:
            list[Pin]: A list of pins that belong to the specified category
        """
