#!/usr/bin/env python3
"""this module is a simple flask web app that has one url"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index() -> str:
    """the function that handles the url for /"""
    return render_template('0-index.html')


if __name__ == '__main__':
    """this ensures that the app only runs when the module is not imported"""
    app.run()
