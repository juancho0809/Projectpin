"""
This file contains the interface of the Catalog class, with its abstract methods

Autor: Edison David Álvarez <edalvarezv@udistrital.edu.co>
"""

from abc import ABC, abstractmethod
from typing import List
from ..board_subsystem.board import Board
from ..board_subsystem.pin import Pin

class CatalogInterface(ABC):
    """
    This is the interface of the Catalog class
    """
    @abstractmethod
    def get_all_boards(self)  -> List[Board]:
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
    def get_all_pins(self) -> List[Pin]:
        """
        This method recovers all the pines from the catalgo boards.

        Returns:
            list[Pin]: A list of all pines in the catalog.
        """

    @abstractmethod
    def add_pin(self, board: Board, pin: Pin):
        """
        This method adds a new pin to a specific board in the catalog.

        Args:
            board (Board): The board to which the pin will be added.
            pin (Pin): The pin object to be added to the board.
        """

    @abstractmethod
    def delete_pin(self, board: Board, pin: Pin):
        """
        This method deletes a pin from a specific board in the catalog.

        Args:
            board (Board): The board from which the pin will be removed.
            pin (Pin): The pin object to be removed from the board.
        """

    @abstractmethod
    def get_board_by_name(self, name: str) -> Board:
        """
        This method retrieves a board by its name.

        Args:
            name (str): The name of the board to retrieve.

        Returns:
            Board: The board with the specified name, or None if not found.
        """

    @abstractmethod
    def get_boards_by_category(self, category: str) -> List[Board]:
        """
        This method retrieves all boards in a specific category from the catalog.

        Args:
            category (str): The category to filter the boards by.

        Returns:
            list[Board]: A list of boards that belong to the specified category.
        """

    @abstractmethod
    def get_pin_by_name(self, name: str) -> Pin:
        """
        This method retrieves a pin by its name from all boards in the catalog.

        Args:
            name (str): The name of the pin to retrieve.

        Returns:
            Pin: The pin with the specified name, or None if not found.
        """

    @abstractmethod
    def get_pins_by_category(self, category: str) -> List[Pin]:
        """
        This method retrieves all pins in a specific category from the catalog.

        Args:
            category (str): The category to filter the pins by.

        Returns:
            list[Pin]: A list of pins that belong to the specified category.
        """
