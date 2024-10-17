#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    _summary_
    """
    return render_template("0-index.html", message="Welcome to Holberton")


if __name__ == '__main__':
    app.run(debug='True')
