#!/usr/bin/python3
"""script that starts a Flask web application"""
from models import storage, state
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/states_list", strict_slashes=False)
def states_list():
    all_states = storage.all(state.State)  # this for fileStorage
    return render_template("7-states_list.html", states=all_states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
