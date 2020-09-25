"""
Constants module.
"""
from pathlib import Path


APP_DIR: Path = Path(__file__).resolve().parent.parent
VAR_DIR: Path = APP_DIR / "var"
WIKI_TABLE_CLASS: str = "wikitable"

WIKI_DOMAIN: str = "wikipedia.org"
DEFAULT_URL: str = "https://en.wikipedia.org/wiki/Python_(programming_language)"
