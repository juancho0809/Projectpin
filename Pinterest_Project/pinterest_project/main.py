from fastapi import FastAPI
from pydantic import BaseModel, SecretStr
import os
from dotenv import load_dotenv



app = FastAPI(

    title="Pinterest Project",
    description="This is a Pinterest Project",
    version="1.0.0",
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


class Login(BaseModel):
    """This class is used to authenticate an user."""
    username: str
    password: SecretStr



@app.post("/login")
def login(user_info: Login) -> bool:
    """This service lets authenticate an user using username and password."""
    # make authentication
    return False


# Services for Manager
@app.get("/admin/watch_catalog")
def watch_scheduling():
    """This service allows to a manager see full scheduling in the center."""
    return None


@app.put("/admin/edit_catalog")
def edit_catalog():
    """This service allows to a manager edit the catalog."""
    return None


# Services for Client
@app.get("/client/show_catalog")
def show_catalog():
    """This service is used to show the courses catalog to clients."""
    return None


@app.post("/client/create_catalog")
def create_catalog():
    """This is a service to create a new catalog on the board."""
    return None


@app.put("/client/edit_own_catalog")
def edit_own_catalog():
    """This is a service to edit the client's own catalog."""
    return None
