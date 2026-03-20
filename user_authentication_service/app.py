#!/usr/bin/env python3
"""This module starts a basic Flask app for the authentication service.

It provides a single route that returns a welcome message in JSON format.
"""

from flask import Flask, jsonify, Response

app = Flask(__name__)

@app.route("/", methods=["GET"])
def welcome() -> Response:
    """Return a JSON response with a welcome message for the user."""
    return jsonify({"message": "Bienvenue"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
