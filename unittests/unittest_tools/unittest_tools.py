"""Tools for unittests."""
import os


def flask_response_data(resp):
    """Flask html response without whitespaces.

    :param resp: app_fixture response"""
    return "".join(resp.data.decode().split())


def open_expected_template(path, template):
    """Expected template depends on url and method.

    :param path: path to template
    :param template: filename of template without extension - by default .html
    """
    with open(os.path.join(path, 'expected_templates', f'{template}.html'), 'r') as templ:
        return "".join(templ.read().split())
