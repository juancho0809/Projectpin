"""
This is the main module of our project where web services will be 
implemented with fastapi from our backend.
Authors: Edison David Alvarez <edalvarezv@udistrital.edu.co>
         Juan Diego Lozada <juandiegolozada123@gmail.com>
"""
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, SecretStr
from .core_subsystem import CatalogProxy
from .board_subsystem import Board, Pin
from .data_base import BoardModel, PinModel
from .data_base.data_base import validate_user, fetch_boards_from_db

boards = fetch_boards_from_db()
catalog = CatalogProxy()
for board in boards:
    catalog.add_board(board)

app = FastAPI(
    title="Pinterest Project",
    description="This is a Pinterest Project",
    version="1.0.0",
)

class Login(BaseModel):
    """This class is used to authenticate an user."""
    username: str
    password: SecretStr

@app.get("/")
def show_catalog_pins() -> List[Pin]:
    """
    This service returns all pins in the catalog.
    """
    return catalog.get_all_boards()

@app.get("/Boards")
def show_catalog_boards() -> List[Board]:
    """
    This service returns all boards in the catalog.
    """
    return catalog.get_all_boards()

@app.post("/login")
def login(user_info: Login) -> bool:
    """
    This service lets users authenticate using their username and password.
    """
    # make authentication
    return validate_user(user_info.username, user_info.password)

# Services for Manager
@app.get("/admin/watch_catalog")
def show_boards() -> List[Board]:
    """
    This service allows a manager to see all boards in the catalog.
    """
    return catalog.get_all_boards()

@app.get("/admin/watch_catalog")
def show_pins() -> List[Pin]:
    """
    This service allows a manager to see all pins in the catalog.
    """
    return catalog.get_all_pins()

@app.put("/admin/delete_board")
def delete_board(id_board: int):
    """
    This service allows a manager to delete a board from the catalog.
    """
    for board in catalog.get_all_boards():
        if board.id_board == id_board:
            catalog.delete_board(board)

@app.put("/admin/delete_pin")
def delete_pin(id_pin: int):
    """
    This service allows a manager to delete a pin from the catalog.
    """
    for pin in catalog.get_all_pins():
        if pin.id == id_pin:
            catalog.delete_pin(pin)

# Services for Client
@app.get("/client/show_catalog")
def show_catalog() -> List[Pin]:
    """
    This service is used to show the pins catalog to clients.
    """
    return catalog.get_all_pins()

@app.put("/client/create_pin")
def create_pin(id_board: int, pin_model: PinModel):
    """
    This service creates a new pin in a specified board.
    """
    pin = instance_pin(pin_model)
    board = find_board(id_board)
    catalog.add_pin(board, pin)

@app.put("/client/delete_pin")
def delete_pin_client(id_pin: int):
    """
    This service deletes a pin from the catalog.
    """
    pin = find_pin(id_pin)
    catalog.delete_pin(pin)

@app.put("/client/create_board")
def create_board(board_model: BoardModel):
    """
    This service creates a new board in the catalog.
    """
    board = instance_board(board_model)
    catalog.add_board(board)

@app.put("/client/search_pin_by_name")
def get_pin_by_name(name: str):
    """
    This service searches for a pin by name.
    """
    return catalog.get_pin_by_name(name)

@app.put("/client/search_pins_by_category")
def get_pins_by_category(category: str):
    """
    This service searches for pins by category.
    """
    return catalog.get_pins_by_category(category)

@app.put("/client/search_board_by_name")
def get_board_by_name(name: str):
    """
    This service searches for a board by name.
    """
    return catalog.get_board_by_name(name)

@app.put("/client/search_board_by_category")
def get_boards_by_category(category: str):
    """
    This service searches for boards by category.
    """
    return catalog.get_boards_by_category(category)

def instance_pin(pin_model: PinModel) -> Pin:
    """
    This function creates a Pin instance from a PinModel.
    """
    id_pin = pin_model.id_pin
    user_id = pin_model.user_id
    name = pin_model.name
    description = pin_model.description
    url = pin_model.url
    categories = pin_model.categories
    pin = Pin(id_pin, user_id, name, description, url)
    for category in categories:
        pin.add_category_pin(category)
    return pin

def instance_board(board_model: BoardModel) -> Board:
    """
    This function creates a Board instance from a BoardModel.
    """
    id_board = board_model.id_pin
    user_id = board_model.user_id
    name = board_model.name
    description = board_model.description
    pins = board_model.pin_list
    categories = board_model.categories
    board = Board(id_board, user_id, name, description)
    for pin in pins:
        pin_instance = instance_pin(pin)
        board.add_pin(pin_instance)
    for category in categories:
        board.add_category_board(category)
    return board

def find_board(id_board: int) -> Board:
    """
    This function finds a board by its ID.
    """
    for board in catalog.get_all_boards():
        if board.id_board == id_board:
            return board

def find_pin(id_pin: int) -> Pin:
    """
    This function finds a pin by its ID.
    """
    for pin in catalog.get_all_pins():
        if pin.id_pin == id_pin:
            return pin
