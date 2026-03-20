#!/usr/bin/env python3
"""Authentication service utilities."""

import bcrypt


def _hash_password(password: str) -> bytes:
    """Return a salted hash of the input password using bcrypt."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

from db import DB
from sqlalchemy.orm.exc import NoResultFound

class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str):
        """Register a new user with email and password.
        Raises ValueError if user already exists.
        Returns the created User object.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed = _hash_password(password)
            return self._db.add_user(email, hashed)
