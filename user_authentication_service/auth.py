"""Authentication service utilities.

This module provides authentication helpers for user management, including password hashing and user registration.
"""

import bcrypt

from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User


def _hash_password(password: str) -> bytes:
    """Hash a password with bcrypt and return the salted hash as bytes.

    Args:
        password (str): The plain text password to hash.

    Returns:
        bytes: The salted hash of the password.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.

    Provides methods for user registration and authentication.
    """

    def __init__(self) -> None:
        """Initialize the Auth class and set up the database handler."""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user with the given email and password.

        Args:
            email (str): The user's email address.
            password (str): The user's password.

        Returns:
            User: The created user object.

        Raises:
            ValueError: If a user with the given email already exists.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(
                "User {} already exists".format(email)
            )
        except NoResultFound:
            hashed = _hash_password(password)
            return self._db.add_user(email, hashed)
