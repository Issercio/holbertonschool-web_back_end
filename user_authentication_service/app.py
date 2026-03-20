#!/usr/bin/env python3
"""Basic Flask app for authentication service.

This module sets up a simple Flask application with a welcome route.
"""

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def welcome() -> 'flask.Response':
    """Return a welcome message as JSON."""
    return jsonify({"message": "Bienvenue"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
