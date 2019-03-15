import pytest

from tools import html_parser, word_counter


@pytest.mark.parametrize(
    'html_input, expected_keywords, expected_text',
    (
        (
            '<html><head><meta name="keywords" content="r2d2, chess, queen" /></head>'
            '<body><p><span>chess</span> <span>r2d2</span></p> <b>queen</b> <i>queen</i> something wrong with chess :)'
            '<script>console.log("chess")</script></body></html>',
            ['r2d2', 'chess', 'queen'],
            'chess r2d2 queen queen something wrong with chess :)',
        ),
        (
            '<html><head></head><body><p><span>chess</span> <span>r2d2</span></p> '
            '<b>queen</b> <i>queen</i> something wrong with chess :)</body></html>',
            [],
            'chess r2d2 queen queen something wrong with chess :)',
        ),
    ),
)
def test_html_parser(html_input, expected_keywords, expected_text):
    keywords, text = html_parser(html_input)
    assert keywords == expected_keywords
    assert text == expected_text


@pytest.mark.parametrize(
    'word_list, text, expected_output',
    (
        (
            ['python', 'foo', 'bar'],
            'hi python word foo bar foo foo xyz, baar www hey hiho wooo',
            {'python': 1, 'foo': 3, 'bar': 1},
        ),
    ),
)
def test_word_counter(word_list, text, expected_output):
    assert word_counter(word_list, text) == expected_output
