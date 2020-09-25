#!/usr/bin/env python
"""
Main application file.
"""
import csv
import sys
from typing import List, Tuple
from pathlib import Path

from requests_html import HTMLSession


APP_DIR = Path(__file__).resolve().parent
VAR_DIR = APP_DIR / "var"
WIKI_TABLE_CLASS = "wikitable"

WIKI_DOMAIN = "wikipedia.org"
DEFAULT_URL = "https://en.wikipedia.org/wiki/Python_(programming_language)"

TextRow = List[str]


def as_text(elements) -> TextRow:
    """
    Exract text from a list of HTML elements.
    """
    return [el.text for el in elements]


def write_csv(path: Path, fieldnames: TextRow, rows: List[TextRow]) -> None:
    """
    Write a CSV file.
    """
    if not rows:
        print("No rows to write")
        print()
        return

    with open(path, "w") as f_out:
        writer = csv.writer(f_out, quoting=csv.QUOTE_ALL, lineterminator="\n")
        writer.writerow(fieldnames)
        writer.writerows(rows)

    print("Wrote CSV:")
    print(f" - {path}")
    print(f" - {len(rows)} data rows")
    print()


def extract_table(table) -> Tuple[TextRow, List[TextRow]]:
    """
    Get values out of an HTML table.
    """
    html_rows = table.find("tr")

    header = html_rows.pop(0)
    fieldnames = as_text(header.find("th"))

    rows = [as_text(row.find("td")) for row in html_rows]

    return fieldnames, rows


def process(url: str) -> None:
    """
    Extract tables on a given URL and write out as CSVs.
    """
    session = HTMLSession()
    r = session.get(url)

    selector = "body table"
    if WIKI_DOMAIN in url:
        selector = f"{selector}.{WIKI_TABLE_CLASS}"

    tables = r.html.find(selector)

    for i, table in enumerate(tables):
        fieldnames, rows = extract_table(table)

        title = str(i + 1)
        out_path = VAR_DIR / f"{title}.csv"
        write_csv(out_path, fieldnames, rows)


def main(args: List[str]) -> None:
    """
    Main command-line function.
    """
    if args:
        url = args[0]
    else:
        url = DEFAULT_URL

    process(url)


if __name__ == "__main__":
    main(sys.argv[1:])
