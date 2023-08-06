#!/bin/python

from re import search


class Clean(str):
    
    @staticmethod
    def html_cleaner(text: str) -> (str):
        from re import compile as com
        from re import sub
        return sub(
            com(
                r'<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});'
                ),
            '',
            text
            )

class Scanner(
    object
    ):
    
    @staticmethod
    def check_type(
        chat_id: str
        ) -> (
            str
            or
            ...
            ):
             
            if len(chat_id) > 2:
                
                if   chat_id[:2].lower() == 'g0':
                    return 'Group'
                elif chat_id[:2].lower() == 'c0':
                    return 'Channel'
                elif chat_id[:2].lower() == 'u0':
                    return 'User'
                elif chat_id[:2].lower() == 's0':
                    return 'Service'
                elif chat_id[:2].lower() == 'b0':
                    return 'Bot'
                else                            :
                    raise ValueError(f'CHAT ID \'{chat_id}\' NOT FOUND!')
            
            else:
                raise ValueError(f'CHAT ID \'{chat_id}\' FALSE!')

class Maker(
    object
    ):

    @staticmethod
    def check_link(link: str, key: str) -> (str):
        from .. import Client
        with Client(key, banner=False) as client:
            
            if link.startswith('@') or search(r'rubika\.ir/\w{4,25}'):

                link: str = link.replace('https://', '').replace('rubika.ir/', '')
                result: dict = client.get_object_by_username(link.replace('@', '')).get('data')
                result: dict = result.get('user') or result.get('channel') or result.get('group')
                return result.get('user_guid') or result.get('channel_guid') or result.get('group_guid')
            
            elif len(link) == 56 or len(link) == 48 and 'joing' in link or 'joinc' in link:
                
                if 'joinc' in link:
                    return client.group_preview_by_join_link(link)['data']['group']['group_guid']
                elif 'joing' in link:
                    return client.channel_preview_by_join_link(link)['data']['channel']['channel_guid']

class Login(
    object
    ):

    @staticmethod
    def SignIn(phone: str) -> (str):
        from .. import Client
        return Client.sign_in(phone, Client.send_code(phone, input('send type is SMS/Interval : '), password=input('please enter your password : ') if input('insert password y/n : ').lower() == 'y' else None).get('data').get('phone_code_hash'), input('please enter activation code : ')).get('data').get('auth') or '0'
    
