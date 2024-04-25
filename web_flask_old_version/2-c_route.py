#!/usr/bin/python3
""" This module starts a Flask app
The app listens on 0.0.0.0 at port 5000.
route ==> /: Displays "Hello HBNB"
route ==> /hbnb: display "HBNB"
route ==> /c/<text>: display “C ” followed by the value of the text variable
                    (replace underscore _ symbols with a space )
"""
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """This function returns 'Hello HBNB'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """This function returns 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space )
    """
    text = text.replace("_", " ")
    return f'C {escape(text)}'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
