"""
This file has the user class

Autor: Edison David Álvarez <edalvarezv@udistrital.edu.co>
"""


class User:
    """This class represents a user"""

    def __init__(
        self, id_user: int, name: str, email: str, password: str, type_user: bool
    ):
        self.id_user = id_user
        self.name = name
        self.email = email
        self.__password = password
        self.type_user = type_user

    def login(self, email, password):
        """
        This method authenticates the user with the provided email and
        password, using a database function

        Arguments:
            email (string): The email address of the user trying to login.
            password (string): The password provided by the user for authentication.

        Returns:
            bool: True if the login credentials are correct; False otherwise.
        """

    def get_password(self):
        """
        This method returns the user's password.

        Returns:
            str: The user's password.
        """
        return self.__password
