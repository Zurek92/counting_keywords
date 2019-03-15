#!/usr/bin/env python3
import os

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
    assert resp._status_code == status_code
    assert open_expected_template(current_path, template) in flask_response_data(resp)
