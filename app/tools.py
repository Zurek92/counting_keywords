#!/usr/bin/env python3
from bs4 import BeautifulSoup


def html_parser(html):
    """Extract keywords and text content without html tags from html structure.

    :param html: html page structure
    """
    soup = BeautifulSoup(html, 'html.parser')
    keywords = soup.find('meta', {'name': 'keywords'}) or {}
    keywords_list = [keyword.strip() for keyword in keywords.get('content', '').split(',') if keyword]
    for tag in soup(['script', 'style']):
        tag.decompose()
    text = soup.get_text()
    return (keywords_list, text)


def word_counter(words_list, text):
    """Counting words in text.

    :param word_list: list with word, which should be counted
    :param text: string where words are counted
    """
    return {word: text.count(word) for word in words_list}
