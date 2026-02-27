#!/usr/bin/env python3
""" Auth class for API authentication
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """ Auth class to manage API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determine if authentication is required for a given path
        Args:
            path: the path to check
            excluded_paths: list of paths that don't require authentication
        Returns:
            False - will be implemented later
        """
        return False

    def authorization_header(self, request=None) -> str:
        """ Get the authorization header from the request
        Args:
            request: Flask request object
        Returns:
            None - will be implemented later
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Get the current user from the request
        Args:
            request: Flask request object
        Returns:
            None - will be implemented later
        """
        return None
