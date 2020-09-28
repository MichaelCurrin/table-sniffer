# Table Sniffer 🕵️ 🕸 🐶 🐽 🗄
> HTML table scraping for CSV lovers

<!-- Shields from https://shields.io/ -->
[![Actions status](https://github.com/MichaelCurrin/table-sniffer/workflows/Python%20application/badge.svg)](https://github.com/MichaelCurrin/table-sniffer/actions)
[![Made with Python](https://img.shields.io/badge/Python->=3.6-blue?logo=python&logoColor=white)](https://python.org)
[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/table-sniffer.svg)](https://GitHub.com/MichaelCurrin/table-sniffer/tags/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](#license)


This simple Python finds HTML tables on a given webpage and saves each as CSV files. It only cares about data as plain text, as it strips out HTML styling, links etc.


## Sample usage

Run the tool against a URL.

```sh
$ python -m table_sniffer.table_sniffer 'https://example.com'
```

If any HTML `table` elements could be found on the page, you'll see log output telling you about the CSVs written out to the project's `var` directory.


## Documentation

Read more in the [docs](/docs/).


## License

Released under [MIT](/LICENSE).
