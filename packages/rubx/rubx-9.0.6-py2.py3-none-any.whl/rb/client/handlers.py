#!/bin/python

from json import dumps, loads
from re import compile as com
from re import findall, search, sub

import websocket

from .. import RubikaClient
from ..crypto import Encryption
from ..rubikaclient import Client
from ..tools import Scanner


class NewMessage(Client):

    def reg(
        self,
        filters: list = None,
        pattern: str = None,
        ) -> (None):
        
        if not isinstance(filters, list):
            filters: list = [filters]
        for message in Client(self.auth, banner=False).handle('handshake', True, True, filters):
            if search(r'%s' % pattern, message.get('text') or message):
                yield message

class EventBuilder(Client):
    
    def __str__(self) -> (str):
        return self.jsonify(indent=2)

    def __getattr__(self, name) -> (list):
        return self.find_keys(keys=name)

    def __setitem__(self, key, value) -> (...):
        self.original_update[key] = value

    def __getitem__(self, key):
        return self.original_update[key]

    def __lts__(self, update: list) -> (list):
        for index, element in enumerate(update):
            if isinstance(element, list):
                update[index] = self.__lts__(update=element)

            elif isinstance(element, dict):
                update[index] = EventBuilder(update=element)

            else:
                update[index] = element
        return update

    def __init__(self, update: dict) -> (...):
        self.original_update = update

    def to_dict(self) -> (dict):
        return self.original_update

    def jsonify(self, indent=None) -> (str):
        
        result = self.original_update
        result['original_update'] = 'dict{...}'
        
        return dumps(
            result,
            indent=indent,
            ensure_ascii=False,
            default=lambda value: str(value)
            )

    def find_keys(self: Client, keys: list,
                  original_update: str = None) -> (list):

        if original_update is None:
            original_update = self.original_update

        if not isinstance(keys, list):
            keys = [keys]

        if isinstance(original_update, dict):
            for key in keys:
                try:
                    update = original_update[key]
                    if isinstance(update, dict):
                        update = EventBuilder(update=update)

                    elif isinstance(update, list):
                        update = self.__lts__(update=update)

                    return update

                except KeyError:
                    pass
            original_update = original_update.values()

        for value in original_update:
            if isinstance(value, (dict, list)):
                try:
                    return self.find_keys(keys=keys, original_update=value)

                except AttributeError:
                    pass

        raise AttributeError(f'Struct object has no attribute {keys}')

    def guid_type(self, chat_id: str) -> str:
        if isinstance(chat_id, str):
            return Scanner.check_type(chat_id)

    @property
    def type(self):
        try:
            return self.find_keys(keys=['type', 'author_type'])

        except AttributeError:
            pass

    @property
    def raw_text(self):
        try:
            return self.find_keys(keys='text')

        except AttributeError:
            pass

    @property
    def message_id(self):
        try:
            return self.find_keys(keys=['message_id',
                                        'pinned_message_id'])
        except AttributeError:
            pass

    @property
    def reply_message_id(self):
        try:
            return self.find_keys(keys='reply_to_message_id')

        except AttributeError:
            pass

    @property
    def is_group(self):
        return self.type == 'Group'

    @property
    def is_channel(self):
        return self.type == 'Channel'

    @property
    def is_private(self):
        return self.type == 'User'

    @property
    def object_guid(self):
        try:
            return self.find_keys(keys=['group_guid',
                                        'object_guid', 'channel_guid'])
        except AttributeError:
            pass

    @property
    def author_guid(self):
        try:
            return self.author_object_guid

        except AttributeError:
            pass
    
    def is_personl(self, chat_id: str) -> (bool):
        if isinstance(chat_id, str):
            if Scanner.check_type(chat_id) == 'User':
                return True
            else:
                return False
    
    def is_group(self, chat_id: str) -> (bool):
        if isinstance(chat_id, str):
            if Scanner.check_type(chat_id) == 'Group':
                return True
            else:
                return False
    
    def is_channel(self, chat_id: str) -> (bool):
        if isinstance(chat_id, str):
            if Scanner.check_type(chat_id) == 'Channel':
                return True
            else:
                return False
    
    def message(
        self            : str = 'Handler',
        chat_type       : str = 'user',
        search_filters  : str = ...,
        find_filters    : str = ...,
        chat_filters   : str = ...
        ) -> (dict):
        
        def show() -> (dict or list[dict, ]):
            
            for msg in self.get_chats_updates() if self.get_chat_updates in list(self.handling.keys()) else self.handling.get(list(self.handling.keys())[0]):
                msg: dict = msg.get('last_message') or  msg
                if search_filters and search(r'%s' % str(search_filters), msg['text']) or find_filters and findall(r'%s' % find_filters, msg['text']):
                    yield msg or {} if chat_filters and chat_type.lower() == 'user' and msg.get('author_object_guid') == chat_filters or chat_type.lower() == 'object' and msg.get('object_guid') == chat_filters else msg or {}
        
    def pin(self, chat_id: str, message_id: str) -> (dict):
        return self.set_pin_message(chat_id=chat_id, message_id=message_id, action='Pin')
    
    def unpin(self, chat_id: str, message_id: str) -> (dict):
        return self.set_pin_message(chat_id=chat_id, message_id=message_id, action='Unpin')

    def seen(self, chat_id: str,
             message: str) -> (dict):
        return self.seen_chats({chat_id: message})
    
    def reply(self, chat_id: str, text: str,
              message: str) -> (dict):
        return self.send_message(text, chat_id, reply_to_message_id=message)
    
    def edit(self, chat_id: str, text: str, message: str) -> (dict):
        return self.edit_message(message, text, chat_id)
    
    def forwards(self, from_: str, to: str, messages: list) -> (dict):
        return self.forward_messages(from_, messages, to)
    
    def download(self, chat_id: str, message: str, name: str) -> (dict):
        return self.get_file('message', True, saveAS='name', chat_id=chat_id, message_id=message)

    def delete(self, chat_id: str,
               messages: list) -> (dict):
        self.delete_messages(messages, chat_id)

class Handler(RubikaClient):
    
    def handle(self, method: str, get_chats: bool = True,
               get_messages: bool = None, chat_ids: str = None,
               author_guid: str = None) -> (dict[str, ]):
        
        if 'handshake' in method.lower():
            
            for msg in self.hand_shake():
                if msg.get('type') == 'messenger':
                    res: dict = Encryption(self.auth).decrypt(msg.get('data_enc'))
                    
                    if get_chats and get_messages:
                        yield res
                    elif get_messages:
                        for i in res.get('message_updates'):
                            yield res
                    elif get_chats:
                        for i in res.get('chat_updates'):
                            yield i

        elif 'getchatupdates' in method.lower():
            for msg in self.get_chats_updates().get('data').get('chats'):
                if chat_ids:
                    if msg.get('last_message').get('object_guid') in chat_ids:
                        return msg.get('last_message')
                else:
                    return msg.get('last_message')
            
        elif 'getmessagesupdates' in method.lower():
            for chat_id in chat_ids:
                for msg in self.get_messages_updates(chat_id).get('data').get('updated_messages'):
                    yield msg.get('last_message')
    
    def hand_shake(self, api_version='4') -> dict:

        for i in range(5):
            try:
                
                websocket.connect('wss://jsocket3.iranlms.ir:80')
                websocket.send(
                        dumps(
                            {
                                'api_version'   :   api_version,
                                'auth'          :   self.auth,
                                'method'        :   'handShake'
                                }
                            )
                        )
                data: str = websocket.recv()
                if len(str(data)) != 33:
                    return loads(data)
                
            except Exception:
                ...

    def handler(
        self    :   'Handler',
        handler :   object
        ) -> (None):
        
        self.on(handler)

    def on(self, event) -> object or (None):
        
        def decorator(func) -> (None):
            self.add_event_handling(func=func, events=event)
            return func

        return decorator

    def add_event_handling(self, **funcs) -> (None):
        self.handling[funcs.get('func')]: object = funcs.get('events')
    
    def remove_event_handling(self, func: object):
        try:
            self.handling.pop(func)
        except KeyError:
            ...
