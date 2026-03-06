#!/usr/bin/env python3
""" Test current_user within API context
"""
from api.v1.auth.session_auth import SessionAuth
from models.user import User
from flask import Flask, request

# Create user
user = User()
user.email = "test_api@test.io"
user.password = "password123"
user.save()
print("Created user: {}".format(user.id))

# Create SessionAuth instance (simulating what happens in api/v1/app.py)
sa = SessionAuth()

# Create session
session_id = sa.create_session(user.id)
print("Created session: {}".format(session_id))
print("Sessions stored: {}".format(sa.user_id_by_session_id))

# Test getting user_id from session_id
retrieved_user_id = sa.user_id_for_session_id(session_id)
print("\nRetrieved user_id: {}".format(retrieved_user_id))

# Test current_user with Flask request context
app = Flask(__name__)
with app.test_request_context('/', headers={'Cookie': '_my_session_id={}'.format(session_id)}):
    retrieved_user = sa.current_user(request)
    if retrieved_user:
        print("SUCCESS! Retrieved user: {} ({})".format(retrieved_user.id, retrieved_user.email))
    else:
        print("FAILED! No user retrieved")
