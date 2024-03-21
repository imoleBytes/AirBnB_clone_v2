#!/usr/bin/python3
""" This module starts a Flask app
The app listens on 0.0.0.0 at port 5000.
route ==> /: Displays "Hello HBNB"
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """This function returns 'hello hbnb'"""
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
