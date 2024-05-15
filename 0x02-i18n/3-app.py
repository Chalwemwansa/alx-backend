#!/usr/bin/env python3
"""this module is a simple flask web app that has one url"""
from flask import Flask, render_template, request
from flask_babel import Babel
from typing import List


class Config:
    """class that specifies the configuratios for our flask web app"""
    LANGUAGES: List[str] = ['en', 'fr']
    BABEL_DEFAULT_LOCALE: str = 'en'
    BABEL_DEFAULT_TIMEZONE: str = 'UTC'


app: Flask = Flask(__name__)
app.config.from_object(Config)
babel: Babel = Babel(app)


@babel.localeselector
def get_locale_func() -> str:
    """function sets the locales to be used in our flask web app"""
    lang: str = request.accept_languages.best_match(app.config.LANGUAGES)
    return lang


@app.route('/')
def index() -> str:
    """the function that handles the url for /"""
    return render_template('3-index.html')


if __name__ == '__main__':
    """this ensures that the app only runs when the module is not imported"""
    app.run()
