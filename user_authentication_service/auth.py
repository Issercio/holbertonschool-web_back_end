#!/usr/bin/env python3
"""Authentication service utilities.

This module provides authentication helpers for user management.
It includes password hashing and user registration.
"""

import bcrypt
import uuid
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


def _generate_uuid() -> str:
    """Generate a new UUID and return its string representation.

    Returns:
        str: The string representation of a new UUID.
    """
    return str(uuid.uuid4())


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
            return self._db.add_user(email, hashed.decode('utf-8'))

    def valid_login(self, email: str, password: str) -> bool:
        """Validate user credentials.

        Args:
            email (str): The user's email address.
            password (str): The user's password.

        Returns:
            bool: True if credentials are valid, False otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password.encode('utf-8'))
        except Exception:
            return False

    def create_session(self, email: str) -> str:
        """Create a new session ID for the user and return it.

        Args:
            email (str): The user's email address.

        Returns:
            str: The session ID, or None if user not found.
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except Exception:
            return None
