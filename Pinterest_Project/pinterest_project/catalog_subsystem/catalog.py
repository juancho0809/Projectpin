"""
This file contains the concrete implementation of catalog, which 
inherits from CatalogInterface

Autor: Edison David Álvarez <edalvarezv@udistrital.edu.co>
"""
from typing import List
from .catalog_interface import CatalogInterface
from ..board_subsystem import Board
from ..board_subsystem import Pin

class Catalog(CatalogInterface):
    """
    This is the specific Catalog class that wound from CatalgoInterface
    """

    def __init__(self):
        self.__board_list = []

    def get_all_boards(self) -> List[Board]:
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

    def get_all_pins(self) -> List[Pin]:
        """
        This method recovers all the pines from the catalgo boards.

        Returns:
            list[Pin]: A list of all pines in the catalog.
        """
        pins = []
        for board in self.__board_list:
            pins.extend(board.get_pins())
        return pins

    def add_pin(self, board: Board, pin: Pin):
        """
        This method adds a new pin to a specific board in the catalog.

        Args:
            board (Board): The board to which the pin will be added.
            pin (Pin): The pin object to be added to the board.
        """
        if board in self.__board_list:
            board.add_pin(pin)

    def delete_pin(self, pin: Pin):
        """
        This method deletes a pin from a specific board in the catalog.

        Args:
            board (Board): The board from which the pin will be removed.
            pin (Pin): The pin object to be removed from the board.
        """
        for board in self.__board_list:
            for pins in board.get_all_pins():
                if pins == pin:
                    board.delete_pin(pin)

    def get_board_by_name(self, name: str) -> Board:
        """
        This method retrieves a board by its name.

        Args:
            name (str): The name of the board to retrieve.

        Returns:
            Board: The board with the specified name, or None if not found.
        """
        for board in self.__board_list:
            if board.name == name:
                return board
        return None

    def get_boards_by_category(self, category: str)  -> List[Board]:
        """
        This method retrieves all boards in a specific category from the catalog.

        Args:
            category (str): The category to filter the boards by.

        Returns:
            list[Board]: A list of boards that belong to the specified category.
        """
        boards_in_category = []
        for board in self.__board_list:
            for categories in board.categories:
                if categories == category:
                    boards_in_category.append(board)
        return boards_in_category

    def get_pin_by_name(self, name: str) -> Pin:
        """
        This method retrieves a pin by its name from all boards in the catalog.

        Args:
            name (str): The name of the pin to retrieve.

        Returns:
            Pin: The pin with the specified name, or None if not found.
        """
        for board in self.__board_list:
            pin = board.get_pin_by_name(name)
            return pin
        return None

    def get_pins_by_category(self, category: str) -> List[Pin]:
        """
        This method retrieves all pins in a specific category from the catalog.

        Args:
            category (str): The category to filter the pins by.

        Returns:
            list[Pin]: A list of pins that belong to the specified category.
        """
        pins_in_category = []
        for board in self.__board_list:
            pins = board.get_pin_by_category(category)
            pins_in_category.extend(pins)
        return pins_in_category
