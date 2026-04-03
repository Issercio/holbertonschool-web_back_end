#!/usr/bin/env python3
"""
Flask app with Babel, forced locale, mock login system, and timezone selection.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz

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


def get_locale():
    """
    Determines the best locale to use for the current request.
    Priority:
    1. Locale from URL parameters
    2. Locale from user settings
    3. Locale from request header
    4. Default locale
    Returns:
        str: The selected locale ('en' or 'fr').
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    user = getattr(g, 'user', None)
    if user:
        user_locale = user.get('locale')
        if user_locale in app.config['LANGUAGES']:
            return user_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_timezone():
    """
    Determines the best timezone to use for the current request.
    Priority:
    1. Timezone from URL parameters
    2. Timezone from user settings
    3. Default to UTC
    Returns:
        str: The selected timezone (must be valid for pytz).
    """
    tz_param = request.args.get('timezone')
    if tz_param:
        try:
            pytz.timezone(tz_param)
            return tz_param
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    user = getattr(g, 'user', None)
    if user:
        user_tz = user.get('timezone')
        if user_tz:
            try:
                pytz.timezone(user_tz)
                return user_tz
            except pytz.exceptions.UnknownTimeZoneError:
                pass
    return 'UTC'


@app.before_request
def before_request():
    """
    Executed before each request to set the user in flask.g if logged in.
    """
    g.user = get_user()


babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route("/")
def index():
    """
    Render the index page with a translated welcome message and login status.
    Returns:
        str: Rendered HTML of the index page with the correct translation
        for the heading and login status.
    """
    return render_template(
        "7-index.html",
        get_locale=get_locale,
        get_timezone=get_timezone
    )


if __name__ == "__main__":
    app.run()
