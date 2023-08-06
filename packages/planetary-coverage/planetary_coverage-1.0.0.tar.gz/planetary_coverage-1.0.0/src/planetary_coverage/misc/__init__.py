"""Miscellaneous module."""

from .cache import cached_property, debug_cache
from .depreciation import DepreciationHelper, depreciated, warn
from .dotenv import debug_env, find_dotenv, getenv
from .download import debug_download, wget
from .list import rindex
from .logger import logger
from .segment import Segment


__all__ = [
    'Segment',
    'logger',
    'rindex',
    'wget',
    'cached_property',
    'depreciated',
    'DepreciationHelper',
    'warn',
    'getenv',
    'find_dotenv',
    'debug_download',
    'debug_cache',
    'debug_env',
]
