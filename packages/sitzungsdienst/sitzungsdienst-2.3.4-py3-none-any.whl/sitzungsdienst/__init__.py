"""
This module is part of the 'sitzungsdienst' package,
which is released under GPL-3.0-only license.
"""

from .regex import COURT_DATES, EXPRESS_DATES, PERSON
from .sta import StA

__all__ = [
    # Main class
    "StA",
    # RegExes
    "COURT_DATES",
    "EXPRESS_DATES",
    "PERSON",
]
