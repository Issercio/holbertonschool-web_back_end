#!/usr/bin/env python3
""" Main 5 - Create user and session for testing
"""
from api.v1.auth.session_auth import SessionAuth
from models.user import User

""" Create a user test """
user_email = "test@test.io"
user_clear_pwd = "test_password"

user = User()
user.email = user_email
user.password = user_clear_pwd
user.first_name = "Test"
user.last_name = "User"
user.save()

print("New user: {}".format(user.id))

""" Create a session ID """
sa = SessionAuth()
session_id = sa.create_session(user.id)
print("Session ID: {}".format(session_id))
print("\nTest with:")
print('curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id={}"'.format(session_id))
