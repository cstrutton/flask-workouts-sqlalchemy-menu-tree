import os

from flask import Flask
from config import config


# every learning journey starts with hello
def index():
    return "hello world"


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    app.add_url_rule('/', 'index', index)
    return app




