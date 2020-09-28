# Table Sniffer 🕵️ 🕸 🐶 🐽 🗄
> HTML table scraping for CSV lovers

<!-- Shields from https://shields.io/ -->
[![Actions status](https://github.com/MichaelCurrin/table-sniffer/workflows/Python%20application/badge.svg)](https://github.com/MichaelCurrin/table-sniffer/actions)
[![Made with Python](https://img.shields.io/badge/Python->=3.6-blue?logo=python&logoColor=white)](https://python.org)
[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/table-sniffer.svg)](https://GitHub.com/MichaelCurrin/table-sniffer/tags/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](#license)


This simple Python finds HTML tables on a given webpage and saves each as CSV files. It only cares about data as plain text, as it strips out HTML styling, links etc.


## Sample usage

Run the tool.

```sh
$ python -m table_sniffer.table_sniffer 'https://example.com'
```

Get CSVs written out to the project's `var` directory.


## Documentation

See the project [docs](/docs/).


## Future development

For now, the CSVs have numeric names and repeat runs on different pages will mean you overwrite data.

### Group CSVs

So I'd like to extend this to group CSVs in a folder based on domain and page or user input.

### Table naming

The basic case is one will not have a lot of names and one can rename them by hand. But what if there are a lot of tables of a page and you are scraping many pages and don't feel like going through each?

Perhaps I can use HTML `h` tags to name the table files rather than just by number.

Maybe I can at least print out text from around the table of show the tables in a summarized text form structure of the page, for context. With the sentence or heading before/after the table.

Maybe the ID, class etc. printed. Or `caption`.


## License

Released under [MIT](/LICENSE).
