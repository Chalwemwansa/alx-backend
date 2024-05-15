#!/usr/bin/env python3
"""this module is a simple flask web app that has one url"""
from flask import Flask, render_template
from flask_babel import Babel
from typing import List


class Config:
    """class that is used to configure the babel instance
    with correct config"""
    LANGUAGES: List[str] = ['en', 'fr']
    BABEL_DEFAULT_LOCALE: str = 'en'
    BABEL_DEFAULT_TIMEZONE: str = 'UTC'


app: Flask = Flask(__name__)
app.config.from_object(Config)
babel: Babel = Babel(app)


@app.route('/')
def index() -> str:
    """the function that handles the url for /"""
    return render_template('1-index.html')


if __name__ == '__main__':
    """this ensures that the app only runs when the module is not imported"""
    app.run()
