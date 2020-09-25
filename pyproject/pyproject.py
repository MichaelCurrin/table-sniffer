#!/usr/bin/env python
"""
Main application file.
"""
import csv
import sys
from typing import List
from pathlib import Path

from requests_html import HTMLSession


APP_DIR = Path(__file__).resolve().parent
VAR_DIR = APP_DIR / "var"
WIKI_TABLE_CLASS = "wikitable"

DEFAULT_URL = "https://en.wikipedia.org/wiki/Python_(programming_language)"


def as_text(elements):
    return [el.text for el in elements]


def write_csv(path: Path, fieldnames: list, rows: List[list]) -> None:
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


def main(args: List[str]):
    """
    Main command-line function.
    """
    if args:
        url = args[0]
    else:
        url = DEFAULT_URL

    session = HTMLSession()
    r = session.get(url)

    selector = "body table"
    selector = f"{selector}.{WIKI_TABLE_CLASS}"

    tables = r.html.find(selector)

    for i, t in enumerate(tables):
        html_rows = t.find("tr")

        header = html_rows.pop(0)
        fieldnames = as_text(header.find("th"))

        rows = [as_text(row.find("td")) for row in html_rows]

        out_path = VAR_DIR / f"{i+1}.csv"
        write_csv(out_path, fieldnames, rows)


if __name__ == "__main__":
    main(sys.argv[1:])
