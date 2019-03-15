from unittest.mock import Mock, patch

import pytest

from main import app
from decorators import check_json, get_content


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


@patch('decorators.requests.get')
def test_get_content(mocked_get):
    mocked_get.return_value.text = '<html><head></head><body></body></html>'

    @get_content
    def some_test_func(user_json):
        return user_json

    assert some_test_func({'url': 'http://google.com'}) == {
        'url': 'http://google.com',
        'content': '<html><head></head><body></body></html>',
    }


@patch('decorators.requests.get', Mock(side_effect=Exception('wrong url :)')))
def test_get_content_failed():
    with app.test_request_context():

        @get_content
        def some_test_func(user_json):
            return user_json

        resp = some_test_func({'url': 'www.wrong.url.com'})
        assert resp.status_code == 400
        assert resp.get_json() == {'status': 400, 'message': 'URL is wrong or page is diabled.'}
