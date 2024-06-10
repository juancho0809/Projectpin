"""
This module contains the responsible decorator
to obtain the performance time of the system.

Autor: Edison David Álvarez <edalvarezv@udistrital.edu.co>
"""
from typing import List
import time
import logging
import psutil
from ..catalog_subsystem.catalog_interface import CatalogInterface
from ..board_subsystem.board import Board
from ..board_subsystem.pin import Pin

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TimePerformanceDecorator(CatalogInterface):
    """
    This class is a decorator to get time performance information
    about the catalog functions.
    """

    def __init__(self, catalog: CatalogInterface):
        """
        Initializes the TimePerformanceDecorator with a CatalogInterface instance.

        Args:
            catalog (CatalogInterface): An instance of the Catalog class to be decorated.
        """
        self.__catalog = catalog

    def get_all_boards(self) -> List[Board]:
        """
        Gets all boards and logs the time taken for the operation.

        Returns:
            list: A list of all boards in the catalog.
        """
        start = time.time()
        result = self.__catalog.get_all_boards()
        end = time.time()
        logger.info("get_all_boards took %s seconds", end - start)
        return result

    def add_board(self, board: Board):
        """
        Adds a board to the catalog and logs the time taken for the operation.

        Args:
            board (Board): The board to be added to the catalog.
        """
        start = time.time()
        self.__catalog.add_board(board)
        end = time.time()
        logger.info("add_board took %s seconds", end - start)

    def delete_board(self, board: Board):
        """
        Deletes a board from the catalog and logs the time taken for the operation.

        Args:
            board (Board): The board to be deleted from the catalog.
        """
        start = time.time()
        self.__catalog.delete_board(board)
        end = time.time()
        logger.info("delete_board took %s seconds", end - start)

    def get_all_pins(self) -> List[Pin]:
        """
        Gets all pins and logs the time taken for the operation.

        Returns:
            list: A list of all pins in the catalog.
        """
        start = time.time()
        result = self.__catalog.get_all_pins()
        end = time.time()
        logger.info("get_all_pins took %s seconds", end - start)
        return result

    def add_pin(self, board: Board, pin: Pin):
        """
        Adds a pin to a specific board in the catalog and logs the time taken 
        for the operation.

        Args:
            board (Board): The board to which the pin will be added.
            pin (Pin): The pin to be added to the board.
        """
        start = time.time()
        self.__catalog.add_pin(board, pin)
        end = time.time()
        logger.info("add_pin took %s seconds", end - start)

    def delete_pin(self, board: Board, pin: Pin):
        """
        Deletes a pin from a specific board in the catalog and logs the
        time taken for the operation.

        Args:
            board (Board): The board from which the pin will be deleted.
            pin (Pin): The pin to be deleted from the board.
        """
        start = time.time()
        self.__catalog.delete_pin(board, pin)
        end = time.time()
        logger.info("delete_pin took %s seconds", end - start)

    def get_board_by_name(self, name: str) -> Board:
        """
        Gets a board by its name and logs the time taken for the operation.

        Args:
            name (str): The name of the board to retrieve.

        Returns:
            Board: The board with the specified name.
        """
        start = time.time()
        result = self.__catalog.get_board_by_name(name)
        end = time.time()
        logger.info("get_board_by_name took %s seconds", end - start)
        return result

    def get_boards_by_category(self, category: str) -> List[Board]:
        """
        Gets boards by category and logs the time taken for the operation.

        Args:
            category (str): The category of boards to retrieve.

        Returns:
            list: A list of boards that belong to the specified category.
        """
        start = time.time()
        result = self.__catalog.get_board_by_category(category)
        end = time.time()  # Record end time
        logger.info("get_board_by_category took %s seconds", end - start)
        return result

    def get_pin_by_name(self, name: str) -> Pin:
        """
        Gets a pin by its name and logs the time taken for the operation.

        Args:
            name (str): The name of the pin to retrieve.

        Returns:
            Pin: The pin with the specified name.
        """
        start = time.time()
        result = self.__catalog.get_pin_by_name(name)
        end = time.time()
        logger.info("get_pin_by_name took %s seconds", end - start)
        return result

    def get_pins_by_category(self, category: str) -> List[Pin]:
        """
        Gets pins by category and logs the time taken for the operation.

        Args:
            category (str): The category of pins to retrieve.

        Returns:
            list: A list of pins that belong to the specified category.
        """
        start = time.time()
        result = self.__catalog.get_pin_by_category(category)
        end = time.time()
        logger.info("get_pin_by_category took %s seconds", end - start)
        return result

class MemoryPerformanceDecorator(CatalogInterface):
    """
    This class is a decorator to get memory performance 
    information about the catalog functions.
    """
    def __init__(self, catalog: CatalogInterface):
        """
        Initializes the MemoryPerformanceDecorator with a CatalogInterface instance.

        Args:
            catalog (CatalogInterface): An instance of a class that implements 
            the CatalogInterface.
        """
        self.__catalog = catalog
        self.__process = psutil.Process()

    def get_all_boards(self) -> List[Board]:
        """
        Retrieves all boards from the catalog and logs the memory consumption 
        of the operation.

        Returns:
            list[Board]: A list of all boards in the catalog.
        """
        start = self.__process.memory_info().rss / 1024
        boards = self.__catalog.get_all_boards()
        end = self.__process.memory_info().rss / 1024
        logger.info("get_all_boards took %s Kb", round((end - start), 2))
        return boards

    def add_board(self, board: Board):
        """
        Adds a new board to the catalog and logs the memory consumption 
        of the operation.

        Args:
            board (Board): The board object to be added to the catalog.
        """
        start = self.__process.memory_info().rss / 1024
        self.__catalog.add_board(board)
        end = self.__process.memory_info().rss / 1024
        logger.info("add_board took %s Kb", round((end - start), 2))

    def delete_board(self, board: Board):
        """
        Deletes a board from the catalog and logs the memory consumption 
        of the operation.

        Args:
            board (Board): The board object to be deleted from the catalog.
        """
        start = self.__process.memory_info().rss / 1024
        self.__catalog.delete_board(board)
        end = self.__process.memory_info().rss / 1024
        logger.info("delete_board took %s Kb", round((end - start), 2))

    def get_all_pins(self) -> List[Pin]:
        """
        Retrieves all pins from the catalog and logs the memory consumption
        of the operation.

        Returns:
            list[Pin]: A list of all pins in the catalog.
        """
        start = self.__process.memory_info().rss / 1024
        pins = self.__catalog.get_all_pins()
        end = self.__process.memory_info().rss / 1024
        logger.info("get_all_pins took %s Kb", round((end - start), 2))
        return pins

    def add_pin(self, board: Board, pin: Pin):
        """
        Adds a new pin to a board in the catalog and logs the memory
        consumption of the operation.

        Args:
            board (Board): The board to which the pin will be added.
            pin (Pin): The pin object to be added to the board.
        """
        start = self.__process.memory_info().rss / 1024
        self.__catalog.add_pin(board, pin)
        end = self.__process.memory_info().rss / 1024
        logger.info("add_pin took %s Kb", round((end - start), 2))

    def delete_pin(self, board: Board, pin: Pin):
        """
        Deletes a pin from a board in the catalog and logs the memory
        consumption of the operation.

        Args:
            board (Board): The board from which the pin will be deleted.
            pin (Pin): The pin object to be deleted.
        """
        start = self.__process.memory_info().rss / 1024
        self.__catalog.delete_pin(board, pin)
        end = self.__process.memory_info().rss / 1024
        logger.info("delete_pin took %s Kb", round((end - start), 2))

    def get_board_by_name(self, name: str) -> Board:
        """
        Retrieves a board by its name from the catalog and logs the memory
        consumption of the operation.

        Args:
            name (str): The name of the board to be retrieved.

        Returns:
            Board: The board object with the specified name.
        """
        start = self.__process.memory_info().rss / 1024
        board = self.__catalog.get_board_by_name(name)
        end = self.__process.memory_info().rss / 1024
        logger.info("get_board_by_name took %s Kb", round((end - start), 2))
        return board

    def get_boards_by_category(self, category: str) -> List[Board]:
        """
        Retrieves boards by category from the catalog and logs the memory
        consumption of the operation.

        Args:
            category (str): The category to filter the boards by.

        Returns:
            list[Board]: A list of boards that belong to the specified category.
        """
        start = self.__process.memory_info().rss / 1024
        boards = self.__catalog.get_boards_by_category(category)
        end = self.__process.memory_info().rss / 1024
        logger.info("get_boards_by_category took %s Kb", round((end - start), 2))
        return boards

    def get_pin_by_name(self, name: str) -> Pin:
        """
        Retrieves a pin by its name from the catalog and logs the memory
        consumption of the operation.

        Args:
            name (str): The name of the pin to be retrieved.

        Returns:
            Pin: The pin object with the specified name.
        """
        start = self.__process.memory_info().rss / 1024
        pin = self.__catalog.get_pin_by_name(name)
        end = self.__process.memory_info().rss / 1024
        logger.info("get_pin_by_name took %s Kb", round((end - start), 2))
        return pin

    def get_pins_by_category(self, category: str) -> List[Pin]:
        """
        Retrieves pins by category from the catalog and logs the memory
        consumption of the operation.

        Args:
            category (str): The category to filter the pins by.

        Returns:
            list[Pin]: A list of pins that belong to the specified category.
        """
        start = self.__process.memory_info().rss / 1024
        pins = self.__catalog.get_pins_by_category(category)
        end = self.__process.memory_info().rss / 1024
        logger.info("get_pins_by_category took %s Kb", round((end - start), 2))
        return pins
