#!/usr/bin/env python3
"""
Flask app with Babel, forced locale, and mock login system.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
_.__doc__ = """
_ is an alias for the gettext translation function provided by Flask-Babel.
It is used to mark strings for translation in the application and templates.
"""


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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel()


def get_user():
    """
    Retrieve a user dictionary based on the login_as URL parameter.
    Returns:
        dict or None: The user dictionary if found, else None.
    """
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """
    Executed before each request to set the user in flask.g if logged in.
    """
    g.user = get_user()

def get_locale():
    """
    Determines the best locale to use for the current request.
    - If the 'locale' URL parameter is present and valid, use it.
    - Otherwise, use the best match from the request's Accept-Language headers.
    Returns:
        str: The selected locale ('en' or 'fr').
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index():
    """
    Render the index page with a translated welcome message and login status.
    Returns:
        str: Rendered HTML of the index page with the correct translation for the heading and login status.
    """
    return render_template(
        "5-index.html",
        get_locale=get_locale
    )


if __name__ == "__main__":
    app.run()
