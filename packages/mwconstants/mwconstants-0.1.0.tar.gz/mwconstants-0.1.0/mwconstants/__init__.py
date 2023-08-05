from mwconstants.constants.c_languages import (
    NON_WHITESPACE_LANGUAGES,
    WIKIPEDIA_LANGUAGES,
)
from mwconstants.links import link_to_namespace

__title__ = "mwconstants"
__summary__ = (
    "mwconstants is a package with various data and utilities for processing wikitext."
)
__url__ = "https://gitlab.wikimedia.org/repos/research/mwconstants"

__version__ = "0.1.0"

__license__ = "MIT License"

__all__ = ["link_to_namespace", "WIKIPEDIA_LANGUAGES", "NON_WHITESPACE_LANGUAGES"]
