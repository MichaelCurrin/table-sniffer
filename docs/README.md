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

This project is built on `requests-html` which uses `requests` and BeautifulSoup internally so you can focus on the higher-level tasks. It also uses a virtual browser so it can run JS, parse the DOM and therefore scrape Single-page Applications or other dynamic tables. Unlike `requests` which reads plain HTML only.


## Alternatives

### Google sheets

This project is inspired by the `IMPORTXML` function in Google Sheets that lets you import a table from an HMTL page.

e.g.

```
IMPORTHTML("http://en.wikipedia.org/wiki/Demographics_of_India", "table", 4)
```

See the [tutorial](https://support.google.com/docs/answer/3093339) in Google's support docs.

### Pandas

You can also get similar functionality with the [Pandas](https://pandas.pydata.org/) package.

```python
import pandas as pd

url = "http://en.wikipedia.org/wiki/Demographics_of_India"

df = pd.read_html(url)
df.to_csv('1.csv')
```

Docs:

- [pd.read_html](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_html.html).   
    > Read HTML tables into a list of DataFrame objects.
    >
    > ...
    >
    > This function searches for `<table>` elements and only for `<tr>` and `<th>` rows and `<td>` elements within each `<tr>` or `<th>` element in the table. `<td>` stands for “table data”. This function attempts to properly handle colspan and rowspan attributes. If the function has a `<thead>` argument, it is used to construct the header, otherwise the function attempts to find the header within the body (by putting rows with only `<th>` elements into the header).
    - Works on HTML is a string variable or a given URL.
    - Tutorials
        - [marsja.se](https://www.marsja.se/how-to-use-pandas-read_html-to-scrape-data-from-html-tables/)
        - [TowardsDataScience.com](https://towardsdatascience.com/scraping-tabular-data-with-pandas-python-10cf2a133cbf)
- [pd.df.to_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html)


## Future development

For now, the CSVs have numeric names and repeat runs on different pages will mean you overwrite data.

### Group CSVs

So I'd like to extend this to group CSVs in a folder based on domain and page or user input.

### Table naming

The basic case is one will not have a lot of names and one can rename them by hand. But what if there are a lot of tables of a page and you are scraping many pages and don't feel like going through each?

Perhaps I can use HTML `h` tags to name the table files rather than just by number.

Maybe I can at least print out text from around the table of show the tables in a summarized text form structure of the page, for context. With the sentence or heading before/after the table.

Maybe the ID, class etc. printed. Or `caption`.
