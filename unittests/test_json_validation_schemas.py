#!/usr/bin/env python3
import pytest
from jsonschema import FormatChecker, validate, ValidationError

from json_validation_schemas import user_json_schema


@pytest.mark.parametrize('user_json', ({'url': 'http://google.com'}, {'url': 'http://www.google.com'}))
def test_user_json_schema(user_json):
    validate(user_json, user_json_schema, format_checker=FormatChecker())


@pytest.mark.parametrize('user_json', ({'url': 'www.google.com'}, {'uurrll': 'http://google.com'}, {}, None))
def test_user_json_schema_failed(user_json):
    with pytest.raises(ValidationError):
        validate(user_json, user_json_schema, format_checker=FormatChecker())
