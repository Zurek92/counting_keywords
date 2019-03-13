#!/usr/bin/env python3
from flask import Flask

from endpoints import endpoint
from errors import error

app = Flask(__name__)
app.register_blueprint(endpoint)
app.register_blueprint(error)
