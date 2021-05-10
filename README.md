# Table Sniffer 🕵️ 🕸 🐶 🐽 🗄
> HTML table scraping for CSV lovers

<!-- Badges from https://michaelcurrin.github.io/badge-generator/ -->

[![Python application](https://github.com/MichaelCurrin/table-sniffer/workflows/Python%20application/badge.svg)](https://github.com/MichaelCurrin/table-sniffer/actions?query=workflow:"Python+application")
[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/table-sniffer?include_prereleases=&sort=semver)](https://github.com/MichaelCurrin/table-sniffer/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)

[![Made with Python](https://img.shields.io/badge/Python->=3.6-blue?logo=python&logoColor=white)](https://python.org)


This simple Python app finds HTML tables on a given webpage and saves each as CSV files. I've tested it on Wikipedia.

The app only cares about getting data as plain text - it strips out any HTML styling, links etc.


## Sample usage

Run the tool against a URL.

```sh
$ python -m table_sniffer.table_sniffer 'https://example.com'
```

If any HTML `table` elements could be found on the page, you'll see log output telling you about the CSVs written out to the project's `var` directory.


## Documentation

<div align="center">
  
[![View - Documentation](https://img.shields.io/badge/View-Documentation-blue?style=for-the-badge)](/docs/)

</div>


## License

Released under [MIT](/LICENSE) by [@MichaelCurrin](https://github.com/MichaelCurrin).
