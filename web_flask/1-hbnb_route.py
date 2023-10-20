#!/usr/bin/python3
"""flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', trict_slashes=False)
def hello_HBNB():
    """display hello world"""
    return 'Hello HBNB!'


@app.route('/hbnb', trict_slashes=False)
def hello_HBNB():
    """display hello world"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
