# Documentation

[![Made with Python](https://img.shields.io/badge/Python->=3.6-blue?logo=python&logoColor=white)](https://python.org)
[![GitHub tag](https://img.shields.io/github/tag/MichaelCurrin/table-sniffer.svg)](https://GitHub.com/MichaelCurrin/table-sniffer/tags/)


## Menu

- [Installation](installation.md)
- [Usage](usage.md)
- [Development](development.md)


## About

Table Sniffer is a light-weight Python 3 tool to help you gather data for your research or data science projects. Point to a page of HTML tables and get CSVs out.

Please scrape responsibly! Follow the user agreements on sites you visit, don't resell the data and don't scrape a site excessively.

### Background

This project is built on `requests-html` which uses `requests` and BeautifulSoup internally so you can focus on the higher-level tasks. It also uses a virtual browser so it can run JS, parse the DOM and therefore scrape Single-page Applications or other dynamic tables. Unlike `requests` which reads plain HTML only.

This project is inspired by the `IMPORTXML` function in Google Sheets that lets you import a table from an HMTL page.

e.g.

```
IMPORTHTML("http://en.wikipedia.org/wiki/Demographics_of_India","table",4)
```

See the [tutorial](https://support.google.com/docs/answer/3093339) in Google's support docs.