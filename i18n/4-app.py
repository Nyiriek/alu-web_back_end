#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _

app = Flask(__name__)


class Config:
    """
    Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale():
    """Best match locale lang"""
    local_lang = request.args.get('locale')
    support_lang = app.config['LANGUAGES']
    if local_lang in support_lang:
        return local_lang
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Index page
    """
    return render_template("0-index.html")


if __name__ == '__main__':
    app.run(debug='True')
