import pytest

from main import app
from decorators import check_json


@pytest.mark.parametrize('user_json', ({'url': 'http://www.google.com'}, {'url': 'http://google.com'}))
def test_check_json(user_json):

    with app.test_request_context(json=user_json):

        @check_json
        def some_test_func(user_json):
            return user_json

        assert some_test_func() == user_json


@pytest.mark.parametrize('user_json', ({}, {'url': 'htttt'}, None))
def test_check_json_failed(user_json):

    with app.test_request_context(json=user_json):

        @check_json
        def some_test_func(user_json):
            return user_json

        assert some_test_func().status_code == 400
