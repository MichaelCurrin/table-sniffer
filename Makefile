default: install install-dev

all: install install-dev checks


h help:
	@grep '^[a-z#]' Makefile


install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

upgrade:
	pip install pip --upgrade
	pip install -r requirements.txt --upgrade
	pip install -r requirements-dev.txt --upgrade


fmt:
	black .
fmt-check:
	black . --diff --check

pylint:
	# Exit on error code if needed.
	pylint table_sniffer || pylint-exit $$?

flake8:
	# Stop the build if there are Python syntax errors or undefined names.
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	# Exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide.
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

lint: pylint flake8

fix: fmt lint

check-types:
	mypy table_sniffer tests

unit:
	pytest

checks: fmt-check lint check-types unit


run:
	# cd table_sniffer && ./table_sniffer.py
	python -m table_sniffer.table_sniffer
