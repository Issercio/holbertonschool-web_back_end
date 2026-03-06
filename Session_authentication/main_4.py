#!/usr/bin/env python3
""" Main 4 - Test current_user with session
"""
from flask import Flask, request
from api.v1.auth.session_auth import SessionAuth
from models.user import User

""" Create a user test """
user_email = "bobsession@hbtn.io"
user_clear_pwd = "fake pwd"

user = User()
user.email = user_email
user.password = user_clear_pwd
user.save()

""" Create a session ID """
sa = SessionAuth()
session_id = sa.create_session(user.id)
print("User with ID: {} has a Session ID: {}".format(user.id, session_id))

""" Create a Flask app and request context """
app = Flask(__name__)

with app.test_request_context('/', headers={'Cookie': '_my_session_id={}'.format(session_id)}):
    """ Get current_user """
    user_retrieved = sa.current_user(request)
    if user_retrieved:
        print("User retrieved: {}".format(user_retrieved.id))
    else:
        print("No user retrieved")
