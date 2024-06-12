import os
from pydantic import BaseModel
from typing import List




class Category(BaseModel):
    idcategory: int
    desccategory: str

class Pin(BaseModel):
    idpin: str
    iduser: str
    name: str
    description: str
    url: str
    idcategory: int
    idboard: int
    categories: List[Category] = []

class Board(BaseModel):
    idboard: int
    name: str
    iduser: str
    idcatalog: str
    categories: List[Category] = []

class Catalog(BaseModel):    
   
    boards: List[Board] = []

class User(BaseModel):
    iduser: str
    idtypeofuser: str
    email: str
    password: str
    boards: List[Board] = []
    pins: List[Pin] = []
