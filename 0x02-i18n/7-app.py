#!/usr/bin/env python3
"""Basic Flask app module"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """default locale and timezone"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app.config.from_object(Config)


@app.route('/')
def hello():
    """hello method"""
    return render_template('7-index.html')


@babel.localeselector
def get_locale():
    """method to determine the best match with our supported languages"""
    local_lang = request.args.get('locale')
    if local_lang and local_lang in app.config['LANGUAGES']:
        return local_lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """a method that deduces the proper time zone"""
    logg = get_user()
    if logg:
        locall = logg['timezone']
    if request.args.get('timezone'):
        locall = request.args.get('timezone')
    try:
        return timezone(local).zone
    except Exception:
        return None


def get_user():
    """Method that returns a user dictionary
        or None if the ID cannot be found"""
    try:
        user_Id = request.args.get('login_as')
        return users[int(user_Id)]
    except Exception:
        return None


@app.before_request
def before_request():
    """before request method"""
    g.user = get_user()


if __name__ == "__main__":
    app.run()
