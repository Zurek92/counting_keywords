#!/usr/bin/env python3
import pytest

from main import app


@pytest.fixture()
def app_fixture():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client


@pytest.mark.parametrize(
    'url_path, status_code, resp_data', (('/', 200, b'Hello World'), ('/wrong/url/path', 404, b'Not Found'))
)
def test_simple_endpoint(app_fixture, url_path, status_code, resp_data):
    resp = app_fixture.get(url_path)
    assert resp._status_code == status_code
    assert resp_data in resp.data
