#!/usr/bin/env python3
import os
from unittest.mock import patch

import pytest

from main import app
from unittest_tools.unittest_tools import flask_response_data, open_expected_template

current_path = os.path.dirname(__file__)


@pytest.fixture()
def app_fixture():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client


@pytest.mark.parametrize(
    'url_path, status_code, template', (('/', 200, 'expected_index'), ('/dd', 404, 'expected_not_found'))
)
def test_simple_endpoint_get(app_fixture, url_path, status_code, template):
    resp = app_fixture.get(url_path)
    assert resp.status_code == status_code
    assert open_expected_template(current_path, template) in flask_response_data(resp)


@pytest.mark.parametrize(
    'url_path, user_json, mocked_response, expected_output, status_code',
    (
        (
            '/keywords',
            {'url': 'http://google.com', 'case_sensitive': True},
            '<html><head><meta name="keywords" content="python, javascript" /></head><body>python '
            '<span>javascript</span><b>python</b> PYTHON</body></html>',
            {'succes': True, 'words': {'python': 2, 'javascript': 1}},
            200,
        ),
        (
            '/keywords',
            {'url': 'http://google.com', 'case_sensitive': False},
            '<html><head><meta name="keywords" content="python, javascript" /></head><body>python '
            '<span>javascript</span><b>python</b> PYTHON</body></html>',
            {'succes': True, 'words': {'python': 3, 'javascript': 1}},
            200,
        ),
        (
            '/keywords',
            {'url': 'http://google.com', 'case_sensitive': True},
            '<html><head></head><body>python ' '<span>javascript</span><b>python</b></body></html>',
            {'status': 200, 'message': 'This page doesn\'t have any keywords.'},
            200,
        ),
    ),
)
@patch('decorators.requests.get')
def test_simple_endpoint_post(
    mocked_get, app_fixture, url_path, user_json, mocked_response, expected_output, status_code
):
    mocked_get.return_value.text = mocked_response
    resp = app_fixture.post(url_path, json=user_json)
    assert resp.status_code == status_code
    assert resp.get_json() == expected_output
