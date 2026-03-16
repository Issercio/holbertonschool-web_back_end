#!/usr/bin/env python3
"""Provide authentication helpers for password handling."""

import bcrypt


def _hash_password(password: str) -> bytes:
    """Return a salted bcrypt hash of the provided password string."""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
