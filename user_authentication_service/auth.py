#!/usr/bin/env python3
"""Authentication service utilities."""

import bcrypt

def _hash_password(password: str) -> bytes:
    """Return a salted hash of the input password using bcrypt."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
