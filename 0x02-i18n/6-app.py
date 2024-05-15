#!/usr/bin/env python3
"""this module is a simple flask web app that has one url"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import List, Dict, Optional


class Config:
    """class that specifies the configuratios for our flask web app"""
    LANGUAGES: List[str] = ['en', 'fr']
    BABEL_DEFAULT_LOCALE: str = 'en'
    BABEL_DEFAULT_TIMEZONE: str = 'UTC'


users: Dict[int, Dict[str, Optional[str]]] = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app: Flask = Flask(__name__)
app.config.from_object(Config)
babel: Babel = Babel(app)


@babel.localeselector
def get_locale_func() -> str:
    """function sets the locales to be used in our flask web app"""
    if 'locale' in request.args:
        if request.args.get('locale') in app.config['LANGUAGES']:
            return request.args.get('locale')
    user: Optional[Dict[str, Optional[str]]] = get_user()
    if user is not None:
        user_locale: Optional[str] = user.get('locale')
        if user_locale is not None and user_locale in app.config['LANGUAGES']:
            return user_locale
    lang: str = request.accept_languages.best_match(app.config['LANGUAGES'])
    return lang if lang else app.config['BABEL_DEFAULT_LOCALE']


def get_user() -> Optional[Dict[str, Optional[str]]]:
    """gets a user from the list of users in the dictionary based on the id"""
    if 'login_as' not in request.args:
        return None
    user_id: int = int(request.args.get('login_as'))
    if user_id not in users.keys():
        return None
    return users.get(user_id)


@app.before_request
def before_request():
    """function that is executed everytime a reuest is to be proessed"""
    g.user = get_user()


@app.route('/')
def index() -> str:
    """the function that handles the url for /"""
    return render_template('6-index.html')


if __name__ == '__main__':
    """this ensures that the app only runs when the module is not imported"""
    app.run()
