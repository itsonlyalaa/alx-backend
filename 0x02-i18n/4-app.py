#!/usr/bin/env python3
"""Basic Flask app module"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """default locale and timezone"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def hello():
    """hello method"""
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """method to determine the best match with our supported languages"""
    local_lang = request.args.get('locale')
    if local_lang and local_lang in app.config['LANGUAGES']:
        return local_lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
