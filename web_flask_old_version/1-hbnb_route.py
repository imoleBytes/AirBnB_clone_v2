#!/usr/bin/python3
""" This module starts a Flask app
The app listens on 0.0.0.0 at port 5000.
route ==> /: Displays "Hello HBNB"
route ==> /hbnb: display "HBNB"
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """This function returns 'Hello HBNB'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """This function returns 'HBNB'"""
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
