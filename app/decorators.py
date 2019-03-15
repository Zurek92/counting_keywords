from functools import wraps

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
