# Usage

```sh
$ cd <PATH_TO_REPO>
$ source venv/bin/activate
```

## Run against default URL

```sh
$ make run
```

## Run against custom URL

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

Open your CSVs stored in the `var` directory.

See a sample output CSV stored in the project.

- [wiki-python.csv](/table_sniffer/var/sample/wiki-python.csv)

For example, for this `table` on the page:

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
