#!/usr/bin/python3
""" Write a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
You must use the option strict_slashes=False in your route definition
"""
from flask import Flask
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
    display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
    The default value of text is “is cool”
    """
    txt = text.replace('_', ' ')
    return f"Python {escape(txt)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
