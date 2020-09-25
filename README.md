# Table Sniffer 🕸 🐶 🐽 🗄
> HTML table scraping for CSV lovers

<!-- Shields from https://shields.io/ -->
[![Actions status](https://github.com/MichaelCurrin/table-sniffer/workflows/Python%20application/badge.svg)](https://github.com/MichaelCurrin/table-sniffer/actions)
[![Made with Python](https://img.shields.io/badge/Python->=3.6-blue?logo=python&logoColor=white)](https://python.org)
[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/table-sniffer.svg)](https://GitHub.com/MichaelCurrin/table-sniffer/tags/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](#license)


## Sample usage

There are many `table` elements on this page and one has the class `wikitable`, which is of interest.

- [en.wikipedia.org/wiki/Python_(programming_language)](https://en.wikipedia.org/wiki/Python_(programming_language))

Run the script against a URL. Make sure to quote your URL to escape characters.

```sh
$ python -m table_sniffer.table_sniffer \
    'https://en.wikipedia.org/wiki/Python_(programming_language)'
Wrote CSV:
 - .../var/1.csv
 - 16 data rows

```

Open your CSVs.

See sample output CSV stored in the project:

- [wiki-python.csv](/table_sniffer/var/sample/wiki-python.csv)


## Documentation

See project [docs](/docs/).


## License

Released under [MIT](/LICENSE).
