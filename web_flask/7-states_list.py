#!/usr/bin/python3
"""script to fetch states list from storage"""
from flask import Flask
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown():
    """close the session after each request"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """get state list from storage"""
    return render_tempelete("7-states_list.htm", states=storage.all(Staet))
