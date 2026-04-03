#!/usr/bin/env python3
"""
Basic Flask app with Babel and template parameterization for i18n.
This app configures Babel for English and French support and uses
translations in templates.
"""

from flask import Flask, render_template, request
# _ is an alias for the gettext translation function provided by Flask-Babel.
# It is used to mark strings for translation in the application and templates.
from flask_babel import Babel, _
_.__doc__ = """
_ is an alias for the gettext translation function provided by Flask-Babel.
It is used to mark strings for translation in the application and templates.
"""
"""
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
    Render the index page with a translated welcome message.
    """
    return render_template("3-index.html", get_locale=get_locale)


if __name__ == "__main__":
    app.run()
