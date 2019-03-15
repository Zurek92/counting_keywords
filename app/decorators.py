from functools import wraps

import requests
from flask import jsonify, request
from jsonschema import FormatChecker, validate, ValidationError

from json_validation_schemas import user_json_schema


def check_json(func):
    """Checking json from user."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            user_json = request.get_json()
            validate(user_json, user_json_schema, format_checker=FormatChecker())
        except ValidationError as exc:
            response = jsonify({'status': 400, 'message': exc.message})
            response.status_code = 400
            return response
        return func(*args, user_json=user_json, **kwargs)

    return wrapper


def get_content(func):
    """Get html content from url."""

    @wraps(func)
    def wrapper(user_json, *args, **kwargs):
        try:
            html_content = requests.get(user_json['url']).text
        except Exception:
            response = jsonify({'status': 400, 'message': 'URL is wrong or page is diabled.'})
            response.status_code = 400
            return response
        return func(*args, user_json={'content': html_content, **user_json}, **kwargs)

    return wrapper
