#!/bin/python

import platform
from os import system

from requests import get


class UpToDate(object):

    @classmethod
    def __init__(cls,
                 version: str, url: str) -> ...:
        cls._ver, cls._url = version, url
    
    def up(cls) -> (str):
        if str(get(cls._url).text) != cls._ver:
            return 'notUpdated'
        else:
            return 'isUpdated'
    
    def user(cls) -> (up):

        if cls.up() != 'isUpdated':
            if input('new version rubx now up to date? y/n : ').upper() == 'Y':
                system('pip install rubx --upgrade')
                if platform.system() == 'Windows':
                    system('cls')
                else:
                    system('clear')
        else:
            ... # is full version