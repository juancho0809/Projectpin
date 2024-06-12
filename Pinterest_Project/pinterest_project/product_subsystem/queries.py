from product import User, SessionFactory
from sqlalchemy.orm import Session

class UserController:
    """Class to control the user table in the database."""
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def add_user(self,iduser,idtypeuser,email,password):
        """This method is used to add a new user to the database.
        
        Args: 
            iduser: str
            idtypeuser: str
            email: str
            password: str
        
        """
        session = self.session_factory()

        new_user = User(iduser=iduser,idtypeofuser=idtypeuser,email=email,password=password)
        session.add(new_user)
        session.commit()
        session.close()
        return new_user

user_controller = UserController(SessionFactory)
new_user_db = user_controller.add_user('123456789','1','juan@gmail.com','123456')
print(new_user_db)