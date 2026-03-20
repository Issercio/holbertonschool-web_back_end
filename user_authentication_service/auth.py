#!/usr/bin/env python3
"""Provide authentication helpers for password handling."""

import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User


def _hash_password(password: str) -> bytes:
    """Return a salted bcrypt hash of the provided password string."""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


class Auth:
        def valid_login(self, email: str, password: str) -> bool:
            """
            Validate user credentials.
            Returns True if email exists and password matches, else False.
            """
            try:
                user = self._db.find_user_by(email=email)
            except NoResultFound:
                return False
            if user:
                return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password.encode('utf-8'))
            return False
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user with the provided email and password.
        If a user already exists with the given email, raises a ValueError with a specific message.
        The password is hashed before storing in the database.
        Returns the created User object.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_pwd = _hash_password(password).decode('utf-8')
            return self._db.add_user(email, hashed_pwd)
