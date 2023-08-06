#!/bin/python

import logging
import typing
import webbrowser
from datetime import datetime
from time import sleep
from warnings import warn

from requests import get

from . import Client
from . import __name__ as base
from .clients import Device, Infos
from .crypto import Encryption
from .network import Urls
from .sessions import SQLiteSession
from .tools import Login, UpToDate


class Version(str):
    __version__ =   '9.0.0'
    __author__  =   'saleh'
    __lisense__ =   'MIT'

class RubikaClient(
    object
    ):

    def __init__(
        self                :   ('Client'),
        session_key         :   (str),
        chat_id             :   (str)                   =   (None),
        username            :   (str)                   =   (None),
        app                 :   (str)                   =   ('rubx'),
        phone_number        :   (str)                   =   (None),
        device              :   (dict)                  =   (Device.defaultDevice),
        proxy               :   (dict)                  =   {'http': 'http://127.0.0.1:9050'},
        your_name           :   (str)                   =   (False),
        city                :   (str)                   =   ('mashhad'),
        banner              :   (bool)                  =   (False),
        creator_channel_open:   (bool)                  =   (False),
        platform            :   (str)                   =   (None),
        api_version         :   (str or int)            =   (None),
        headers             :   (dict or str or list)   =   (None),
        timeout             :   (int)                   =   (5),
        check_update        :   (bool)                  =   (False),
        lang_code           :   (str)                   =   ('fa'),
        base_logger         :   (typing.Union[str, logging.Logger])                   =   (None)
        ) -> (
            ...
            ):
        
        '''
        ### the main class
        ## inserts
        
        # USE:
        
            `client = Client('session-key')`
        
        # EXAMPLE:
            
            `with Client(...) as client:`
                `client.send_message(...)`
            
        
        # PARAMETERS:
        
            - 1- `self`: is a self obejct
            - 2- `session_key`: is account key [auth]
            - 3- `chat_id`: is your guid account
            - 4 - `username`: is your username account
            - 5 - `app`: is from app name
            - 6 - `phone_number`: is for using lib with phone_number and geting account key
            - 7 - `device`: is your account device for use token or thumbinline or ...
            - 8 - `your_name`: is for save info in a file.
            - 9 - `city`: is for your countery and city for using client server.
            - 10 - `banner`: is a boolean for print banner
            - 11 - `creator_channel_open`: is for joining your account in creator channel
            - 12 - `platform`: is for using user platform. examples: `rubx` or `web` or `android`
            - 13 - `api_version`: is for using api mode: `5` (for web and rubx) `4` (for rubika app [andorid]) `3` (for m.rubka.ir)
            - 14 - `headers`: is for set header to requests
            - 15 - `timeout`: is for requests timeout
            - 16 - `check_update`: is for checking lib new version
            - 17 - `lang_code`: to app lang code. `en`, `fa`, ...
            - 18 - `base_logger`: is for `__name__`
        '''
        
        (
            self.app,
            self.proxy,
            self.enc,
            self.city,
            self.platform,
            self.api_version,
            self.headers,
            self.username,
            self.chat_id,
            self.handling,
            self.phone,
            _log,
            self.timeout,
            self.lang_code,
            self.device
            ) = (
                app,
                proxy,
                Encryption(session_key),
                city,
                platform,
                api_version,
                headers,
                username,
                chat_id,
                {},
                phone_number,
                logging.getLogger(__name__),
                timeout,
                lang_code,
                device
                )
        
        Infos.citys.append(
            city
            )
        Infos.proxys.append(
            proxy
            )
        
        if banner:
            assert list(map(lambda character: (print(character, flush=True, end=''), sleep(0.01)), f'\n\033[0m< \033[31mrubx \033[0m> \033[36m | \033[31mstarted in \033[0m{str(datetime.datetime.now())}\033[31m| \033[0m{Version.__version__}\n'))
        
        if your_name:
            open('session_info.sty', 'w+').write('name fan: '+your_name+'\ntime started: '+str(datetime.datetime.now())+f'\key: {session_key}'+'\nyour ip: '+str(get('https://api.ipify.org').text))
        
        if session_key:
            self.auth: (str) = (session_key)
            Infos.auth_.append(session_key)
        
        elif phone_number:
            Login.SignIn(phone_number)
            
        else:
            warn('SessionWarning: please insert session key or phone_number in object')
            
        if creator_channel_open:
            
            self.set_channel_action('c0BGS8Y01535a4510be64fafc4610d43', 'Join')
            webbrowser.open('https://rubika.ir/theClient')

        if app == 'rubx':
            
            database = SQLiteSession(session_key)
            database.insert(self.phone, session_key, self.chat_id, Urls.get_url())

        if check_update:
            UpToDate(Version.__version__, 'https://raw.githubusercontent.com/Mester-Root/rubx/main/rubx/__version__').user()
        
        if isinstance(base_logger, str):
            base_logger: str = logging.getLogger(base_logger)
        elif not isinstance(base_logger, logging.Logger):
            base_logger: str = base

        class Loggers(dict):
            def __missing__(self, key) -> ...:
                if key.startswith('rub.'):
                    key = key.split('.', maxsplit=1)[1]

                return base_logger.getChild(key)

        self._log = Loggers()
        
    def __call__(
        self
        ) -> ...:
        ...

    def __enter__(
        self    :   (
            'Client'
            )
        ):
        return (
            self
            )

    def __exit__(
        self    :   ('Client'),
        *args,
        **kwargs
        ) -> ...:
        ...

    def get_auth(self) -> (str or ...):
        return self.auth