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
$ python -m table_sniffer.table_sniffer \
    'https://en.wikipedia.org/wiki/Python_(programming_language)'
Wrote CSV:
 - .../var/1.csv
 - 16 data rows
```
