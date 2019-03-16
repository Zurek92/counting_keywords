#!/usr/bin/env python3
from flask import Flask

from endpoints import endpoint

app = Flask(__name__)
app.register_blueprint(endpoint)
