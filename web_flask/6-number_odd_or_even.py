#!/usr/bin/python3
""" Write a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
You must use the option strict_slashes=False in your route definition
"""
from flask import Flask
from flask import render_template
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """view function for the index route or page"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """view function for the hbnb page"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """
    display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space)
    """
    txt = text.replace('_', ' ')
    return f"C {escape(txt)}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py_text(text='is cool'):
    """
    display “Python ”, followed by the value of the text
    variable (replace underscore _ symbols with a space )
    The default value of text is “is cool”
    """
    txt = text.replace('_', ' ')
    return f"Python {escape(txt)}"


@app.route("/number/<int:n>", strict_slashes=False)
def display_n(n):
    """
    display “n is a number” only if n is an integer
    """
    if isinstance(n, int):
        return f"{escape(n)} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    display a HTML page only if n is an integer:
    H1 tag: “Number: n” inside the tag BODY
    """
    if isinstance(n, int):
        return render_template("5-number.html", num=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """
    display a HTML page only if n is an integer:
    H1 tag: “Number: n is even|odd” inside the tag BODY
    """
    if isinstance(n, int):
        return render_template("6-number_odd_or_even.html", num=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
