from abc import abstractmethod,ABC
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine, delete
from prueba import TypeOfUser, Category, Pin, User, Catalog, Board, category_board_table, category_pin_table
from basemodel import User, Board, Pin
from basemodel import Pin as SQLAlchemyPin, Category
from basemodel import Board as SQLAlchemyBoard  # Importa el modelo Pin correcto de SQLAlchemy
from basemodel import Pin as PydanticPin
from basemodel import Board as PydanticBoard


# Database setup
DATABASE_CONNECTION = 'sqlite:///data.db'
db_conn = create_engine(DATABASE_CONNECTION)
Session = sessionmaker(bind=db_conn)
session = Session()

class InsertDataInterface(ABC):
    """
    This class is used to insert data into the database.
    """
    @abstractmethod
    def create_user_types():
        """
        This method is used to insert data into the TypeOfUser table.
        """
        pass

    @abstractmethod
    def create_categories():
        """This method is used to insert data into the Category table."""
        pass

    @abstractmethod
    def insert_user():
        """This method is used to insert data into the User table."""
        pass

    @abstractmethod
    def insert_catalog():
        """This method is used to insert data into the Catalog table."""
        pass

    @abstractmethod
    def insert_board():
        """This method is used to insert data into the Board table."""
        pass

    @abstractmethod
    def insert_pin():
        """This method is used to insert data into the Pin table."""
        pass

    @abstractmethod
    def insert_category_pin():
        """This method is used to insert data into the category_pin_table."""
        pass

    @abstractmethod
    def insert_category_board():
        """This method is used to insert data into the category_board_table."""
        pass


class InsertData(ABC):
    """
    This class is used to insert data into the database.
    """
    @classmethod
    def create_user_types():
        """
        This method is used to insert data into the TypeOfUser table.
        """
        user_types_data = [
            {"idtypeofuser": "01", "desctypeofuser": "Admin"},
            {"idtypeofuser": "02", "desctypeofuser": "User"}
        ]
        for data in user_types_data:
            new_type = TypeOfUser(**data)
            session.add(new_type)
        session.commit()

    @classmethod
    def create_categories():
        """This method is used to insert data into the Category table."""
        categories_data = [
            {"idcategory": 1, "desccategory": "Action"},
            {"idcategory": 2, "desccategory": "Fantasy"},
            {"idcategory": 3, "desccategory": "Sci-Fi"},
            {"idcategory": 4, "desccategory": "Food"},
            {"idcategory": 5, "desccategory": "Travel"},
            {"idcategory": 6, "desccategory": "Art"}
        ]
        for data in categories_data:
            new_category = Category(**data)
            session.add(new_category)
        session.commit()

    @classmethod
    def insert_user():
        """This method is used to insert data into the User table."""
        user_data= [
            {"iduser": "01", "idtypeofuser": "01", "email": "juan@gmail.com", "password": "1234"},
            {"iduser": "02", "idtypeofuser": "02", "email": "admin@gmail.com", "password": "0809"}
        ]
        for data in user_data:
            new_user = User(**data)
            session.add(new_user)
        session.commit()

    @classmethod
    def insert_catalog():
        """This method is used to insert data into the Catalog table."""
        # Insert data into a catalog table
        catalog_data = [
            {"idcatalog": 1, "name": "The unic one", "description": "Catalog of Boards/Pins"}
        ]
        for data in catalog_data:
            new_catalog = Catalog(**data)
            session.add(new_catalog)
        session.commit()

    @classmethod
    def insert_board():
        """This method is used to insert data into the Board table."""
        # Inserta data into a board table
        board_data = [
            {"idboard": 1, "name": "Board Food", "iduser": "01", "idcatalog": 1},
            {"idboard": 2, "name": "Board Travel", "iduser": "02", "idcatalog": 1},
            {"idboard": 3, "name": "Board Art", "iduser": "02", "idcatalog": 1},
            {"idboard": 4, "name": "Board Sci-Fi", "iduser": "01", "idcatalog": 1}
        ]
        for data in board_data:
            new_board = Board(**data)
            session.add(new_board)
        session.commit()

    @classmethod
    def insert_pin():
        """This method is used to insert data into the Pin table."""
        
        pin_data = [
            {"idpin":1, "iduser": "01", "name": "Pin1", "description": "Description of Pin1", "url": "escudoud.com", "idboard": 1, "idcategory": 4},
            {"idpin":2, "iduser": "02", "name": "Pin2", "description": "Description of Pin2", "url": "pinsci-fi.com", "idboard": 2, "idcategory": 5},
            {"idpin":3, "iduser": "02", "name": "Pin3", "description": "Description of Pin3", "url": "pinart.com", "idboard": 3, "idcategory": 6},
            {"idpin":4, "iduser": "01", "name": "Pin4", "description": "Description of Pin4", "url": "pinfood.com", "idboard": 4, "idcategory": 4},
            {"idpin":5, "iduser": "01", "name": "Pin5", "description": "Description of Pin5", "url": "pintravel.com", "idboard": 2, "idcategory": 5}
        ]
        for data in pin_data:
            new_pin = Pin(**data)
            session.add(new_pin)
        session.commit()

    @classmethod
    def insert_category_pin():
        """This method is used to insert data into the category_pin_table."""
       
        category_pin_data = [
            {"idcategory": 1, "idpin": 1},
            {"idcategory": 2, "idpin": 2},
            {"idcategory": 3, "idpin": 3},
            {"idcategory": 4, "idpin": 4},
            {"idcategory": 5, "idpin": 5}
        ]
        for data in category_pin_data:
            session.execute(category_pin_table.insert().values(data))
        session.commit()

    @classmethod
    def insert_category_board():
        """This method is used to insert data into the category_board_table (tabla many-many)."""
        category_board_data = [
            {"idcategory": 1, "idboard": 1},
            {"idcategory": 2, "idboard": 2},
            {"idcategory": 3, "idboard": 3},
            {"idcategory": 4, "idboard": 4},
            {"idcategory": 5, "idboard": 2},
            {"idcategory": 6, "idboard": 3}
        ]
        for data in category_board_data:
            session.execute(category_board_table.insert().values(data))
        session.commit()


class PinDAO():
    """This is a class to represent a pin as DAO"""

    @classmethod
    def get_all_pins():
        """This method is used to get all pins from the database."""
        pins = session.query(Pin).all()
        for pin in pins:
            print(pin.name)
    
    @classmethod
    def get_all_pins_by_board(idboard:int):
        """This method is used to get all pins by board from the database."""
        pins = session.query(Pin).filter(Pin.idboard == idboard)
        for pin in pins:
            print(pin.name)

    @classmethod
    def add_pin(pin:Pin):
        """This method is used to add a pin to the database."""
        session.add(pin)
        session.commit()

    @classmethod
    def delete_pin(idpin:int):
        """This method is used to delete a pin from the database."""
        session.query(Pin).filter(Pin.idpin == idpin).delete()
        session.commit()

    @classmethod
    def add_pin(cls, session: Session, pin_data: PydanticPin):
        """
        This method is used to add a pin to the database.
        
        Args:
            session (Session): The SQLAlchemy session object.
            pin_data (PydanticPin): The Pydantic model of the pin to be added.
        """
        # Create a new instance of the SQLAlchemy Pin model
        new_pin = SQLAlchemyPin(
            idpin=pin_data.idpin,
            iduser=pin_data.iduser,
            name=pin_data.name,
            description=pin_data.description,
            url=pin_data.url,
            idcategory=pin_data.idcategory,
            idboard=pin_data.idboard
        )
        
        # Add categories relationships if any
        if pin_data.categories:
            for category in pin_data.categories:
                category_instance = session.query(Category).filter_by(idcategory=category.idcategory).first()
                if category_instance:
                    new_pin.categories.append(category_instance)

        # Add the new pin to the session and commit
        session.add(new_pin)
        session.commit()


class BoardDAO():
    """This is a class to represent a board as DAO"""

    @classmethod
    def get_all_boards():
        """This method is used to get all boards from the database."""
        boards = session.query(Board).all()
        for board in boards:
            print(board.name)
    
    @classmethod
    def get_all_boards_by_user(iduser:str):
        """This method is used to get all boards by user from the database."""
        boards = session.query(Board).filter(Board.iduser == iduser)
        for board in boards:
            print(board.name)


    @classmethod 
    def delete_board(idboard:int):
        """This method is used to delete a board from the database."""
        session.query(Board).filter(Board.idboard == idboard).delete()
        session.commit()

    @classmethod
    def add_board(cls, session: Session, board_data: PydanticBoard):
        """
        This method is used to add a board to the database.
        
        Args:
            session (Session): The SQLAlchemy session object.
            board_data (PydanticBoard): The Pydantic model of the board to be added.
        """
        # Create a new instance of the SQLAlchemy Board model
        new_board = SQLAlchemyBoard(
            idboard=board_data.idboard,
            name=board_data.name,
            iduser=board_data.iduser,
            idcatalog=board_data.idcatalog
        )
        
        # Add categories relationships if any
        if board_data.categories:
            for category in board_data.categories:
                category_instance = session.query(Category).filter_by(idcategory=category.idcategory).first()
                if category_instance:
                    new_board.categories.append(category_instance)

        # Add the new board to the session and commit
        session.add(new_board)
        session.commit()

class UserDAO():
    """This is a class to represent a user as DAO"""

    @classmethod
    def get_all_users():
        """This method is used to get all users from the database."""
        users = session.query(User).all()
        for user in users:
            print(user.email)
    
    @classmethod
    def get_user_by_id(iduser:str):
        """This method is used to get a user by id from the database."""
        user = session.query(User).filter(User.iduser == iduser).first()
        print(user.email)

    @classmethod
    def validate_login(email:str, password:str):
        """This method is used to validate login from the database."""
        user = session.query(User).filter(User.email == email, User.password == password).first()
        if user:
            return True
        else:
            return None


