#!/usr/bin/env python3
from flask import Blueprint, jsonify, render_template

from decorators import check_json, get_content
from tools import html_parser, word_counter

endpoint = Blueprint('endpoint', __name__)


@endpoint.route('/', methods=['GET'])
def index():
    """Index page - render form."""

    return render_template('index.html')


@endpoint.route('/keywords', methods=['POST'])
@check_json
@get_content
def keywords_endpoint(user_json):
    """Endpoint which counts keywords in html page."""

    keywords_list, text = html_parser(user_json['content'])
    if not keywords_list:
        return jsonify({'status': 200, 'message': 'This page doesn\'t have any keywords.'})
    return jsonify({'succes': True, 'words': word_counter(keywords_list, text, user_json['case_sensitive'])})
