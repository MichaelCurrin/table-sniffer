# Table Sniffer 🕵️ 🕸 🐶 🐽 🗄
> HTML table scraping for CSV lovers

<!-- Shields from https://shields.io/ -->
[![Actions status](https://github.com/MichaelCurrin/table-sniffer/workflows/Python%20application/badge.svg)](https://github.com/MichaelCurrin/table-sniffer/actions)
[![Made with Python](https://img.shields.io/badge/Python->=3.6-blue?logo=python&logoColor=white)](https://python.org)
[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/table-sniffer.svg)](https://GitHub.com/MichaelCurrin/table-sniffer/tags/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](#license)


## Sample usage

Find a URL which has tables you want to scrape.

- [en.wikipedia.org/wiki/Python_(programming_language)](https://en.wikipedia.org/wiki/Python_(programming_language))

It actually has many `table` elements but only one is of interest and has `wikitable` on the class. So Table Sniffer will see the domain is Wikipedia and filter to only those tables.

Then run the script against a URL. Make sure to quote your URL to escape characters.

```sh
$ python -m table_sniffer.table_sniffer \
    'https://en.wikipedia.org/wiki/Python_(programming_language)'
Wrote CSV:
 - .../var/1.csv
 - 16 data rows

```

Open your CSVs stored in the `var` directory.

See a sample output CSV stored in the project:

- [wiki-python.csv](/table_sniffer/var/sample/wiki-python.csv)


## Documentation

See project [docs](/docs/).


## License

Released under [MIT](/LICENSE).
