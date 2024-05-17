#!/usr/bin/python3
""" Write a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
You must use the option strict_slashes=False in your route definition
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """view function for the index route or page"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """view function for the hbnb page"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
