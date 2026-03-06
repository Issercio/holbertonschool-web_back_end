#!/usr/bin/env python3
""" SessionAuth class for session-based authentication
"""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """ SessionAuth class that inherits from Auth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Create a Session ID for a user_id
        Args:
            user_id: User ID to create session for
        Returns:
            Session ID string, or None if user_id is invalid
        """
        if user_id is None:
            return None
        
        if not isinstance(user_id, str):
            return None
        
        # Generate a Session ID using uuid4()
        session_id = str(uuid4())
        
        # Store the session_id -> user_id mapping
        self.user_id_by_session_id[session_id] = user_id
        
        return session_id
