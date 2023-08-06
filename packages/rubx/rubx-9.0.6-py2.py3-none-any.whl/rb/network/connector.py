#!/bin/python

from json import dumps, loads
from random import choice, randint

from requests import session

from .. import Client
from ..crypto import Encryption
from ..exceptions import *
from ..sessions import SQLiteSession


class Urls(
    (str)
    ):
    
    def get_url() -> str:
        return choice(list(loads(__import__('urllib').request.urlopen('https://getdcmess.iranlms.ir/').read().decode('utf-8')).get('data').get('API').values()))
    
    giveUrl = lambda mode, key=None: SQLiteSession(key).information()[3] if key and 'https://' in SQLiteSession(key).information() else ('https://messengerg2c{}.iranlms.ir/'.format(str('56' if mode.lower() == 'mashhad' else '74' if mode.lower() == 'tehran' else str(randint(3, 74)))))

class clients(
    dict
    ):
    (
        web,
        android,
        rubx
        ) = (
            {
                'app_name'      :   'Main',
                'app_version'   :   '4.1.11',
                'platform'      :   'Web',
                'package'       :   'web.rubika.ir',
                'lang_code'     :   'fa'
                },
            {
                'app_name'      :   'Main',
                'app_version'   :   '2.8.1',
                'platform'      :   'Android',
                'package'       :   'ir.resaneh1.iptv',
                'lang_code'     :   'fa'
                },
            {
                'app_name'      :   'Main',
                'app_version'   :   '3.0.8',
                'platform'      :   'Android',
                'package'       :   'app.rbmain.a',
                'lang_code'     :   'en'
                }
        )

class Make(
    object,
    ):
    
    def evolution(message, key) -> (dict):
        
        res: dict = loads(Encryption(key).decrypt(message.get('data_enc')))
        
        if Errors.MadeError(res.get('status') or '', res.get('status_det') or ''):
            return res

class Connection(
    (
        dict
        )
    ):

    @staticmethod
    def postion(
        url     :   (str),
        data    :   (dict),
        proxy   :   (dict),
        auth    :   (str),
        mode    :   (bool) = (False)
        ) -> (
            dict
            ):

            if (mode):
                from urllib3 import PoolManager, ProxyManager, exceptions
                Make.evolution((ProxyManager(proxy).request('POST', url, body=dumps(data)).data))

            else:
                with session() as (
                    sent
                    ):

                    for (item) in (range(3)):
                        
                        try:
                            return (Make.evolution((sent).post(url, json=dumps(data), proxies=proxy, timeout=5).json(), (auth)))
                        except Exception:
                            ...
                        finally:
                            raise ServerError('the server not response.')

                    else:
                        return 'Not connect to server, Try again.'

class GetData(
    (str)
    ):
    
    @staticmethod
    def api(
        **kwargs
        ) -> (
            Connection
            ):
        '''
        version =   '5' or '4',
        auth    =   'key',
        tmp     =   ...
        method  =   'methodName'
        data    =   input,
        mode     =  'mashhad',
        platform=   'rubx' or 'web',
        proxy   =   {'https':'127.0.0.1:9050'} # a dictionary type
        
        
        '''
        main: list = []
        
        if (kwargs.get('version') == '5'):
            main.extend(
                [
                    {
                        'api_version'   :   '5',
                        '{}'.format('auth' if kwargs.get('auth') else 'tmp_session') :   kwargs.get('auth') or kwargs.get('tmp'),
                        'data_enc'      :   Encryption(kwargs.get('auth')).encrypt(dumps({'input': kwargs.get('data'), 'client': clients.web if kwargs.get('platform') == 'web' else clients.rubx, 'method': kwargs.get('method')}))
                        }
                    ]
                )
        
        else:
            main.extend(
                [
                    {
                        'api_version'   :   '4',
                        'auth'          :   kwargs.get('auth'),
                        'client'        :   clients.android,
                        'method'        :   kwargs.get('method'),
                        'data_enc'      :   Encryption(kwargs.get('auth')).encrypt(dumps(kwargs.get('data')))
                }
                    ]
                )

        return (Connection.postion(Urls.giveUrl(kwargs.get('mode'), kwargs.get('auth')), main[0], kwargs.get('proxy'), kwargs.get('auth')))
    
class Method(
    Client
    ):

    def from_json(
        self       : Client,
        method_name: str,
        **kwargs
        ) -> (
            dict
            ):

            data: dict = {}
            
            assert map(lambda key: data.update({key: kwargs.get(key)}, list(kwargs.keys())))

            return (
                GetData.api(
                    version     =   self.api_version or '5',
                    method      =   method_name[0].lower() + method_name[1:],
                    auth        =   self.auth,
                    data        =   data,
                    proxy       =   self.proxy,
                    platform    =   self.plaform or 'rubx',
                    mode        =   self.city
                )
            )
