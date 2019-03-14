#!/usr/bin/env python3
from flask import Blueprint, render_template

endpoint = Blueprint('endpoint', __name__)


@endpoint.route('/', methods=['GET'])
def index():
    return render_template('index.html')
