from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from dotenv import load_dotenv
import os

Base = declarative_base()

# Table to represent the many-to-many relationship between Category and Pin
category_pin_table = Table('category_pin', Base.metadata,
    Column('idcategory', Integer, ForeignKey('category.idcategory'), 
    primary_key=True, nullable=False),
    Column('idpin', String(5), ForeignKey('pin.idpin'), primary_key=True, nullable=False)
)

# Table to represent the many-to-many relationship between Category and Board
category_board_table = Table('category_board', Base.metadata,
    Column('idcategory', Integer, ForeignKey('category.idcategory'),
    primary_key=True, nullable=False),
    Column('idboard', Integer, ForeignKey('board.idboard'), primary_key=True, nullable=False)
)

class Catalog(Base):
    """Class to represent the Catalog table in the database."""
    __tablename__ = 'catalog'
    idcatalog = Column(String(5), primary_key=True)
    name = Column(String(30), nullable=False)
    description = Column(String(120), nullable=True)
    boards = relationship('Board', back_populates='catalog')

class Pin(Base):
    """Class to represent the Pin table in the database."""
    __tablename__ = 'pin'
    idpin = Column(String(5), primary_key=True)
    iduser = Column(String(12), ForeignKey('user.iduser'), nullable=False)
    name = Column(String(30), nullable=False)
    description = Column(String(120), nullable=True)
    url = Column(String(50), nullable=False)
    idcategory = Column(Integer, ForeignKey('category.idcategory'), nullable=False)
    idboard = Column(Integer, ForeignKey('board.idboard'), nullable=True)
    user = relationship('User', back_populates='pins')
    board = relationship('Board', back_populates='pins')
    categories = relationship('Category', secondary=category_pin_table, back_populates='pins')

class Category(Base):
    """Class to represent the Category table in the database."""
    __tablename__ = 'category'
    idcategory = Column(Integer, primary_key=True)
    desccategory = Column(String(30), nullable=False)
    pins = relationship('Pin', secondary=category_pin_table, back_populates='categories')
    boards = relationship('Board', secondary=category_board_table, back_populates='categories')

class Board(Base):
    """Class to represent the Board table in the database."""
    __tablename__ = 'board'
    idboard = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    iduser = Column(String(12), ForeignKey('user.iduser'), nullable=False)
    idcatalog = Column(String(5), ForeignKey('catalog.idcatalog'), nullable=False)
    user = relationship('User', back_populates='boards')
    catalog = relationship('Catalog', back_populates='boards')
    pins = relationship('Pin', back_populates='board')
    categories = relationship('Category', secondary=category_board_table, back_populates='boards')

class TypeOfUser(Base):
    """Class to represent the TypeOfUser table in the database."""
    __tablename__ = 'typeofuser'
    idtypeofuser = Column(String(2), primary_key=True)
    desctypeofuser = Column(String(30), nullable=False)
    users = relationship('User', back_populates='typeofuser')

class User(Base):
    """Class to represent the User table in the database."""
    __tablename__ = 'user'
    iduser = Column(String(12), primary_key=True)
    idtypeofuser = Column(String(2), ForeignKey('typeofuser.idtypeofuser'), nullable=False)
    email = Column(String(30), nullable=False)
    password = Column(String(15), nullable=False)
    typeofuser = relationship('TypeOfUser', back_populates='users')
    pins = relationship('Pin', back_populates='user')
    boards = relationship('Board', back_populates='user')

# Database setup
load_dotenv()

DATABASE_CONNECTION = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_URL')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
db_conn = create_engine(DATABASE_CONNECTION)
Base.metadata.create_all(db_conn)

# Create a new session
Session = sessionmaker(bind=db_conn)
session = Session()
