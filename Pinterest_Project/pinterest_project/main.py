from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, SecretStr
from sqlalchemy.orm import Session
from product_subsystem import UserController, SessionFactory

app = FastAPI(
    title="Pinterest Project",
    description="This is a Pinterest Project",
    version="1.0.0",
)

def get_session():
    """Dependency that provides a new session per request."""
    session = SessionFactory()
    try:
        yield session
    finally:
        session.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}

class Login(BaseModel):
    """This class is used to authenticate a user."""
    iduser: str
    idtypeuser: str
    email: str
    password: SecretStr

@app.post("/login")
def login(login: Login, session: Session = Depends(get_session)):
    """This service lets authenticate a user using username and password."""
    
    user_controller = UserController(session)
    try:
        user_add = user_controller.add_user(
            iduser=login.iduser,
            idtypeuser=login.idtypeuser,
            email=login.email,
            password=login.password.get_secret_value()
        )
        return {"message": "User added successfully", "user": user_add.iduser}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error adding user: {str(e)}")

# Services for Manager
@app.get("/admin/watch_catalog")
def watch_scheduling():
    """This service allows a manager to see full scheduling in the center."""
    return None

@app.put("/admin/edit_catalog")
def edit_catalog():
    """This service allows a manager to edit the catalog."""
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
