#!/usr/bin/python3
""" This module starts a Flask app
The app listens on 0.0.0.0 at port 5000.
route ==> /: Displays "Hello HBNB"
route ==> /hbnb: display "HBNB"
route ==> /c/<text>: display “C ” followed by the value of the text variable
                    (replace underscore _ symbols with a space )
route ==> /python/<text>: display “Python ” followed by the value of the text
                        variable (replace underscore _ symbols with a space )
route ==> /number/<n>: display “n is a number” only if n is an integer
route ==> /number_template/<n>: display a HTML page only if n is an integer
"""
from flask import Flask
from flask import render_template
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
def c_text(text):
    """display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space )
    """
    text = text.replace("_", " ")
    return f'C {escape(text)}'


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """display “Python ” followed by the value of the text variable
    (replace underscore _ symbols with a space )
    """
    text = text.replace("_", " ")
    return f'Python {escape(text)}'


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """display “n is a number” only if n is an integer"""
    if type(n) == int:
        return f"{escape(n)} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display a HTML page only if n is an integer"""
    if type(n) == int:
        return render_template("5-number.html", num=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
