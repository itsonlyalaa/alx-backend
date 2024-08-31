#!/usr/bin/env python3
"""Basic Flask app module"""
from flask import Flask, render_template

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
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
