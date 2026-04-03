#!/usr/bin/env python3
"""
Basic Flask app with Babel setup for i18n.
This app configures Babel for English and French support.
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Config class for Flask app internationalization settings.
    LANGUAGES: Supported languages for the app.
    BABEL_DEFAULT_LOCALE: Default locale for Babel.
    BABEL_DEFAULT_TIMEZONE: Default timezone for Babel.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app: Flask = Flask(__name__)
app.config.from_object(Config)
babel: Babel = Babel(app)


@app.route("/")
def index() -> str:
    """
    Render the index page with a welcome message.
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
