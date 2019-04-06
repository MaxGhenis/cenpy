__version__ = '1.0.0dev'
__author__ = 'Levi John Wolf levi.john.wolf@gmail.com'

from . import explorer
from .remote import APIConnection as _APIConnection
from .tools import _load_sitekey

SITEKEY = _load_sitekey()

#__all__ = ['explorer', 'base']
