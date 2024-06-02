"""
This file contains the interface of the Catalog class, with its abstract methods

Autor: Edison David Álvarez <edalvarezv@udistrital.edu.co>
"""

from abc import ABC, abstractmethod
from ..board_subsystem.board import Board

class CatalogInterface(ABC):
    """
    This is the interface of the Catalog class
    """

    @abstractmethod
    def get_all_boards(self):
        """
        This method retrieves all boards from the catalog.

        Returns:
            list[Board]: A list of all boards in the catalog.
        """

    @abstractmethod
    def add_board(self, board: Board):
        """
        This method adds a new board to the catalog.
        
        Args:
            board (Board): The board object to be added to the catalog.
        """

    @abstractmethod
    def delete_board(self, board: Board):
        """
        This method deletes a board from the catalog.

        Args:
            board (Board): The board object to be deleted from the catalog.
        """

    @abstractmethod
    def get_all_pins(self):
        """
        This method recovers all the pines from the catalgo boards.

        Returns:
        list[Pin]: A list of all pines in the catalog.
        """

    @abstractmethod
    def get_board_by_category(self, category: str):
        """
        This method  retrieves all boards in a specific category from the catalog.

        Args:
            category (str): The category to filter the boards by.

        Returns:
            list[Board]: A list of boards that belong to the specified category.
        """

    @abstractmethod
    def get_pin_by_category(self, category: str):
        """
        This method retrieves all pins in a specific category from the catalog.

        Args:
            category (str): The category to filter the pins by.

        Returns:
            list[Pin]: A list of pins that belong to the specified category
        """
