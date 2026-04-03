#!/usr/bin/env python3
"""
Basic Flask app with Babel and locale selection for i18n.
This app configures Babel for English and French support.
It selects locale from the request.
"""
from flask import Flask, render_template, request
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
babel: Babel = Babel()


def get_locale() -> str:
    """
    Select the best match language from the request.
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index() -> str:
    """
    Render the index page with a welcome message.
    """
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()
