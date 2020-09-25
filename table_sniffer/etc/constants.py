"""
Constants module.
"""
from pathlib import Path


APP_DIR = Path(__file__).resolve().parent.parent
VAR_DIR = APP_DIR / "var"
WIKI_TABLE_CLASS = "wikitable"

WIKI_DOMAIN = "wikipedia.org"
DEFAULT_URL = "https://en.wikipedia.org/wiki/Python_(programming_language)"
