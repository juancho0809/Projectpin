"""
This module is responsible for implementing the functions of the database
Authors: Edison David Alvarez <edalvarezv@udistrital.edu.co>
         Juan Diego Lozada <juandiegolozada123@gmail.com>
"""
from typing import List
import sqlite3
from ..board_subsystem import Board, Pin

# Conectar a la base de datos
conn = sqlite3.connect("data.db")
cursor = conn.cursor()


def insert_pin(
    idpin: int,
    iduser: int,
    name: str,
    description: str,
    url: str,
    idcategory: int,
    idboard: int,
):
    """
    Inserts a new pin into the database.

    Args:
        idpin (str): The unique identifier for the pin.
        iduser (str): The user identifier who owns the pin.
        name (str): The name of the pin.
        description (str): The description of the pin.
        url (str): The URL associated with the pin.
        idcategory (int): The category identifier to which the pin belongs.
        idboard (int): The board identifier where the pin is placed.
    """
    cursor.execute(
        """
        INSERT INTO pin (idpin, iduser, name, description, url, idcategory, idboard)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
        (idpin, iduser, name, description, url, idcategory, idboard),
    )
    conn.commit()
    conn.close()


def insert_board(name: str, iduser: int, idcatalog: int):
    """
    Inserts a new board into the database.

    Args:
        name (str): The name of the board.
        iduser (str): The user identifier who owns the board.
        idcatalog (str): The catalog identifier to which the board belongs.
    """
    cursor.execute(
        """
        INSERT INTO board (name, iduser, idcatalog)
        VALUES (?, ?, ?)
    """,
        (name, iduser, idcatalog),
    )
    conn.commit()
    conn.close()


def validate_user(email: str, password: str):
    """
    Validates a user's credentials and retrieves user information.

    Args:
        email (str): The email of the user.
        password (str): The password of the user.

    Returns:
        dict: A dictionary containing user information if credentials are valid, otherwise None.
    """
    cursor.execute(
        """
        SELECT user.iduser, user.email, typeofuser.desctypeofuser
        FROM user
        JOIN typeofuser ON user.idtypeofuser = typeofuser.idtypeofuser
        WHERE user.email = ? AND user.password = ?
    """,
        (email, password),
    )
    result = cursor.fetchone()
    if result:
        return {"iduser": result[0], "email": result[1], "typeofuser": result[2]}
    else:
        return None

    conn.close()


def insert_category(idcategory: int, desccategory: str):
    """
    Inserts a new category into the database.

    Args:
        idcategory (int): The unique identifier for the category.
        desccategory (str): The description of the category.
    """
    cursor.execute(
        """
        INSERT INTO category (idcategory, desccategory)
        VALUES (?, ?)
    """,
        (idcategory, desccategory),
    )
    conn.commit()


def insert_category_pin(idcategory: int, idpin: int):
    """
    Inserts a new relationship between a category and a pin into the database.

    Args:
        idcategory (int): The category identifier.
        idpin (str): The pin identifier.
    """
    cursor.execute(
        """
        INSERT INTO category_pin (idcategory, idpin)
        VALUES (?, ?)
    """,
        (idcategory, idpin),
    )
    conn.commit()


def get_next_category_id():
    """
    Retrieves the next available category ID.

    Returns:
        int: The next available category ID.
    """
    cursor.execute(
        """
        SELECT MAX(idcategory) FROM category
    """
    )
    result = cursor.fetchone()
    if result[0] is not None:
        next_id = result[0] + 1
    else:
        next_id = 1
    return next_id


def get_categories_by_pin(idpin: int):
    """
    Retrieves all categories associated with a specific pin.

    Args:
        idpin (str): The pin identifier.

    Returns:
        list: A list of dictionaries containing category information.
    """
    cursor.execute(
        """
        SELECT category.idcategory, category.desccategory
        FROM category
        JOIN category_pin ON category.idcategory = category_pin.idcategory
        WHERE category_pin.idpin = ?
    """,
        (idpin,),
    )
    results = cursor.fetchall()
    categories = [{"idcategory": row[0], "desccategory": row[1]} for row in results]
    return categories


def delete_pin(idpin: int):
    """
    Deletes a pin and its related category_pin relationships from the database.

    Args:
        idpin (int): The pin identifier.
    """
    cursor.execute(
        """
        DELETE FROM category_pin WHERE idpin = ?
    """,
        (idpin,),
    )
    cursor.execute(
        """
        DELETE FROM pin WHERE idpin = ?
    """,
        (idpin,),
    )
    conn.commit()


def get_next_pin_id():
    """
    Retrieves the next available pin ID.

    Returns:
        str: The next available pin ID in the format 'PXXX'.
    """
    cursor.execute(
        """
        SELECT MAX(CAST(SUBSTR(idpin, 2) AS INTEGER)) FROM pin
    """
    )
    result = cursor.fetchone()
    if result[0] is not None:
        next_id = result[0] + 1
    else:
        next_id = 1
    return f"P{next_id:03}"


def get_next_board_id():
    """
    Retrieves the next available board ID.

    Returns:
        int: The next available board ID.
    """
    cursor.execute(
        """
        SELECT MAX(idboard) FROM board
    """
    )
    result = cursor.fetchone()
    if result[0] is not None:
        next_id = result[0] + 1
    else:
        next_id = 1  # Si no hay boards, comenzar desde 1
    return next_id


def fetch_boards_from_db() -> List[Board]:
    """
    Fetches all boards and their associated pins and categories from the database.

    Returns:
        list: A list of Board objects populated with their associated pins and categories.
    """

    # Query to fetch all boards
    cursor.execute("SELECT idboard, iduser, name, description FROM board")
    board_rows = cursor.fetchall()

    # Query to fetch all pins
    cursor.execute(
        "SELECT idpin, iduser, name, description, url, idcategory, idboard FROM pin"
    )
    pin_rows = cursor.fetchall()

    # Query to fetch all categories
    cursor.execute("SELECT idcategory, desccategory FROM category")
    category_rows = cursor.fetchall()

    # Query to fetch category_pin relationships
    cursor.execute("SELECT idcategory, idpin FROM category_pin")
    category_pin_rows = cursor.fetchall()

    # Query to fetch category_board relationships
    cursor.execute("SELECT idcategory, idboard FROM category_board")
    category_board_rows = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Create dictionaries to store instances
    boards_dict = {}
    pins_dict = {}
    categories_dict = {}

    # Create category instances
    for idcategory, desccategory in category_rows:
        categories_dict[idcategory] = desccategory

    # Create pin instances and associate categories
    for idpin, iduser, name, description, url, idcategory, idboard in pin_rows:
        pin = Pin(idpin, iduser, name, description, url)
        if idcategory in categories_dict:
            pin.add_category_pin(categories_dict[idcategory])
        pins_dict[idpin] = pin

    # Create board instances and associate categories
    for idboard, iduser, name, description in board_rows:
        board = Board(idboard, iduser, name, description)
        boards_dict[idboard] = board

    # Associate pins to boards
    for pin in pins_dict.values():
        if pin.board_id in boards_dict:
            boards_dict[pin.board_id].add_pin(pin)

    # Associate categories to boards
    for idcategory, idboard in category_board_rows:
        if idboard in boards_dict and idcategory in categories_dict:
            boards_dict[idboard].add_category_board(categories_dict[idcategory])

    # Add categories to pins
    for idcategory, idpin in category_pin_rows:
        if idpin in pins_dict and idcategory in categories_dict:
            pins_dict[idpin].add_category_pin(categories_dict[idcategory])

    # Return the list of boards
    return list(boards_dict.values())
