#!/bin/python

from .main import RubikaClient, Version
from .rubikaclient import Client

__version__ = Version.__version__

__all__ = [
    'Client',
    'Version',
    'RubikaClient'
]