
# Development

Ensure you have dev dependencies installed as per [Dev Dependencies](installation.md#dev-dependencies) install instructions.

## Commands

### Run all checks

```sh
$ make check
```

### Format

```sh
$ make fmt
```

### Lint

```sh
$ make lint
```

### Check types

```sh
$ make check-types
```

### Run tests

```sh
$ make unit
```


## Scraping dependencies

Instead of using the traditional webscraping combination of _requests_ and _BeautifulSoup_, this app uses the more modern [requests-html][] library as a replacement.

It is by the same author as _requests_ and the main advantage I think is that it can load JS and scrape a rendered DOM, so you don't have to care about the overhead of Selenium and some headless browser.

[requests-html]: https://requests-html.kennethreitz.org/
