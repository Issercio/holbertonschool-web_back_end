#!/usr/bin/env python3
""" Module of Session Authentication views
"""
from flask import jsonify, request, abort
from api.v1.views import app_views
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login() -> str:
    """ POST /api/v1/auth_session/login
    Handle session authentication login
    Return:
      - User object JSON represented with session cookie set
      - Error messages with appropriate status codes
    """
    # Get email and password from form data
    email = request.form.get('email')
    password = request.form.get('password')
    
    # Validate email
    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400
    
    # Validate password
    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400
    
    # Search for user by email
    users = User.search({"email": email})
    
    # Check if user exists
    if not users or len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    
    user = users[0]
    
    # Validate password
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    
    # Import auth only when needed (avoid circular import)
    from api.v1.app import auth
    
    # Create session ID for the user
    session_id = auth.create_session(user.id)
    
    # Get session name from environment variable
    session_name = getenv('SESSION_NAME')
    
    # Create response with user JSON
    response = jsonify(user.to_json())
    
    # Set cookie in response
    response.set_cookie(session_name, session_id)
    
    return response
