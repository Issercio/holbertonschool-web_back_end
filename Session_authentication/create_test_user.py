#!/usr/bin/env python3
""" Create test user for session auth
"""
from models.user import User

# Create test user
user = User()
user.email = "bobsession@hbtn.io"
user.password = "fake pwd"
user.first_name = None
user.last_name = None
user.save()

print("Test user created: {}".format(user.id))
print("Email: {}".format(user.email))
