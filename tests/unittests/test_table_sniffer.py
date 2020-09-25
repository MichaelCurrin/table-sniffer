"""
Test table sniffer.
"""
from collections import namedtuple

from table_sniffer.table_sniffer import as_text


def test_as_text():
    el = namedtuple("element", "text")
    html_elements = [el(text="foo"), el(text="bar"), el(text="buzz")]
    text_items = as_text(html_elements)

    assert text_items == ["foo", "bar", "buzz"]
