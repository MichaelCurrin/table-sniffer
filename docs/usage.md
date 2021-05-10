# Usage

Activate your virtual environment before running commands here.

```sh
$ cd PATH_TO_REPO
$ source venv/bin/activate
```

## Run against default URL

An easy test without having to supply URL. This will Wikipedia's Python page, as set in [constants.py](/table_sniffer/etc/constants.py).

```sh
$ make run
```

## Run against a custom URL

```sh
$ python -m table_sniffer.table_sniffer MY_URL
```


## Tutorial

Find a URL which has tables you want to scrape.

- [en.wikipedia.org/wiki/Python_(programming_language)](https://en.wikipedia.org/wiki/Python_(programming_language))

It actually has many `table` elements but only one is of interest and has `wikitable` on the class. So Table Sniffer will see the domain is Wikipedia and filter to only those tables.

Then run the script against a URL. Make sure to quote your URL to escape characters.

```sh
$ python -m table_sniffer.table_sniffer \
    'https://en.wikipedia.org/wiki/Python_(programming_language)'
```
You'll see output logged for each CSV - `1.csv`, `2.csv`, etc.

```
Wrote CSV:
 - .../var/1.csv
 - 16 data rows

```

Open your CSVs which are stored in the `var` directory.


## Sample

Given this `table` element on the Python Wikipedia page:

```html
<table class="wikitable">
    <caption>Summary of Python 3's built-in types
    </caption>

    <tbody>
        <tr>
            <th>Type</th>
            <th>
                <a href="/wiki/Immutable_object" title="Immutable object">Mutability</a>
            </th>
            <th>Description</th>
            <th style="width: 23em;">Syntax examples</th>
        </tr>
        <tr>
            <!-- Row data -->
            <td>Foo</td>
            <td>Bar</td>
            <td>Baz</td>
            <td>...</td>
        </tr>
        <!-- More rows -->
    </tbody>
</table>
```

You get a CSV like this:

```
Type,Mutability,Description,Syntax examples
Foo,Bar,Baz,...
```

A sample CSV from that page is provided in this repo:

- [wiki-python.csv](/table_sniffer/var/sample/wiki-python.csv)
