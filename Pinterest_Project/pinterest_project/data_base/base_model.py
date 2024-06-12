"""
This file represents the BaseModel of the system classes.

Authors: Edison David Alvarez <edalvarezv@udistrital.edu.co>
         Juan Diego Lozada <juandiegolozada123@gmail.com>
"""

from typing import List
from pydantic import BaseModel

class Pin(BaseModel):
    """
    This class represents the model of the Pin object, which can be considered
    as an image
    """
    id_pin: str
    user_id: int
    name: str
    description: str
    url: str
    categories: List[str] = []

class Board(BaseModel):
    """
    This class represents the model of the Board object,
    which can be considered as a collection of images
    """
    id_board: int
    user_id: int
    name: str
    description: str
    pin_list: List[Pin] = []
    categories: List[str] = []

class Catalog(BaseModel):
    """
    This class represents the model of the Catalog object,
    which can be considered as a collection of boards
    """
    board_list: List[Board] = []

class User(BaseModel):
    """
    This class represents a User.

    """
    id_user: int
    name: str
    email: str
    password: str
    type_user: bool
