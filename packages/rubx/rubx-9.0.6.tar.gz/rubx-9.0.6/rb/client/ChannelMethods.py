#!/bin/python

from os import path

if __name__ == '__main__' and  __package__ == None or __package__ == '':
    import sys
    sys.path.append(path.join(path.dirname(__file__), '..'))
else:
    
    pass
    # import exceptions
    # raise exceptions.MainError('sorry! error in module imports please run app with: `python -m`')

import typing

from ..network import GetData

if typing.TYPE_CHECKING:
    from .. import Client

class ChannelMethods:
    
    def __enter__(
        self    :   (
            'Client'
            )
        ):
        return (
            self
            )

    def __exit__(
        self    :   (
            'Client'
            ),
        *args,
        **kwargs
        ) -> (...):
        ...
    
    set_channel_link        =   lambda self, chat_id: GetData.api(version=self.api_version or '5', method='setChannelLink', auth=self.auth, data={'channel_guid': chat_id}, mode=self.city, platform=self.platform or 'web', proxy=self.proxy)
    check_channel_username  =   lambda self, username: GetData.api(version=self.api_version or '5', method='checkChannelUsername', auth=self.auth, data={'username': username}, mode=self.city, platform=self.platform or 'web', proxy=self.proxy)
    delete_channel          =   lambda self, chat_id: GetData.api(version=self.api_version or '5', method='removeChannel', auth=self.auth, data={'channel_guid': chat_id}, mode=self.city, platform=self.platform or 'web', proxy=self.proxy)

    def add_channel_members(
    
        self        :   'Client',
        user_ids    :   (list),
        chat_id     :   (str)
        ) -> (
            dict
            ):

            '''

            self.add_channel_members(['user guid', ]. chat_id='channel guid')
            
            PARAMETERS:
                1- user_ids a list user guids
                3- chat_id is channel guid
            '''

            return (GetData.api(
                version     =   self.api_version or '5',
                method      =   'addChannelMembers',
                auth        =   self.auth,
                data        =   {
                    'channel_guid'  :   chat_id,
                    'member_guids'  :   user_ids
                    },
                mode        =   self.city,
                platform    =   self.platform or 'web',
                proxy       =   self.proxy
                )
                    )
    
    def get_channel_all_members(
        self            :   ('Client'),
        chat_id         :   (str)   =   (None),
        search_text     :   (str)   =   (None),
        start_id        :   (str)   =   (None)
        ) -> (
            dict
            or
            ...
            ):
            
            '''
            self.get_channel_all_members(...)
            '''

            return (
                GetData.api(
                    version     =   self.api_version or '5',
                    method      =   'getChannelAllMembers',
                    auth        =   self.auth,
                    data        =   {
                        'channel_guid'  :   chat_id,
                        'search_text'   :   search_text,
                        'start_id'      :   start_id
                        },
                    mode        =   self.city,
                    proxy       =   self.proxy,
                    platform    =   self.platform or 'web'
                )
            )
    
    def set_channel_action(
        self    :   Client,
        chat_id :   str,
        action  :   str =   'Join'
        ) -> (
            dict or ...
            ):

            '''
            this method for join and leave channels
            
            USE:
                self.set_action_chat('chat-guid', 'Pin')
            PARAMS:
                1- self is a self object
                2- chat_id is chat guid
                3- action is a action type. actions: 'Join', 'Leave'
            '''

            return (
                GetData.api(
                    version     =   self.api_version or '5',
                    auth        =   self.auth,
                    method      =   'joinChannelAction',
                    data        =   {
                        'channel_guid'   :   chat_id,
                        'action'        :   action
                        },
                    mode        =   self.city,
                    platform    =   self.platfrom or 'web',
                    proxy       =   self.proxy
                )
            )

    def add_channel(
        self            : Client,
        title           : str,
        description     : str,
        channel_type    : str   =   'Public'
        ) -> (
            dict or ...
            ):
            
            '''
            this method for create channel
            
            USE:
                self.add_channel('title', 'bio')
            PARAMS:
                1- self is a self object
                2- title is channel name
                3- description is channel bio
                4- channel_type is a action type for channel. types: 'Public', 'Private'
            '''
            
            return (
                GetData.api(
                    version     =   self.api_version or '5',
                    auth        =   self.auth,
                    method      =   'addChannel',
                    data        =   {
                        'title'         :   title,
                        'description'   :   description,
                        'channel_type'  :   channel_type
                        },
                    mode        =   self.city,
                    platform    =   self.platfrom or 'web',
                    proxy       =   self.proxy
                )
            )

    def edit_channnel_info(
        self    :   Client,
        chat_id :   str,
        **kwargs:   dict or str
        ) -> (
            dict or ...
            ):

            '''
            USE:
                self.edit_channnel_info('chat-guid', title='name')
            PARAMS:
                sign_messages, title, description
            '''

            return (
                GetData.api(
                    version     =   self.api_version or '5',
                    auth        =   self.auth,
                    method      =   'editChannelInfo',
                    data        =   {
                        'updated_parameters'        :   list(kwargs.keys())
                        }.update(kwargs),
                    mode        =   self.city,
                    platform    =   self.platfrom or 'web',
                    proxy       =   self.proxy
                )
            )

    def update_channel_username(
        self    :   Client,
        chat_id :   str,
        username:   str
        ) -> (
            dict or ...
            ):
            
            '''
            self.update_channel_username('channel-guid', 'username')
            '''
            
            return (
                GetData.api(
                    version     =   self.api_version or '5',
                    auth        =   self.auth,
                    method      =   'updateChannelUsername',
                    data        =   {
                        'channel_guid'  :   chat_id,
                        'username'      :   username
                        },
                    mode        =   self.city,
                    platform    =   self.platfrom or 'web',
                    proxy       =   self.proxy
                )
            )

    def set_channel_admin(self: Client, chat_id: str, member_guid: str,
                          access_list: list = None, action: str = 'SetAdmin') -> (dict or ...):
        
        '''
        this method is for admin and unadmin a member chat
        
        
        USE:
            self.set_channel_admin('group-guid', 'user-guid', [accesses.admin.sendMessages])
        
        PARAMS:
            1- self a is self object
            2- chat_id is group guid
            3- member_guid is a user guid
            4- access_list is for access user in group: from rub import accesses.admin or ["ChangeInfo", "ViewMembers", "ViewAdmins", "PinMessages", "SendMessages", "EditAllMessages", "DeleteGlobalAllMessages", "AddMember", "SetJoinLink"]
            5- action is action type: 'UnsetAdmin', 'SetAdmin'
        '''
        
        return (
                GetData.api(
                    version     =   self.api_version or '5',
                    auth        =   self.auth,
                    method      =   'setChannelAdmin',
                    data        =   {
                        'channel_guid'  :   chat_id,
                        'member_guid'   :   member_guid,
                        'action'        :   action,
                        'access_list'   :   access_list
                        },
                    mode        =   self.city,
                    platform    =   self.platfrom or 'web',
                    proxy       =   self.proxy
                )
            )

    def channel_preview_by_join_link(self: Client, link: str) -> (dict):
        
        '''
        get channel info from link
        '''
        
        return (
                GetData.api(
                    version     =   self.api_version or '5',
                    auth        =   self.auth,
                    method      =   'channelPreviewByJoinLink',
                    data        =   {
                        'hash_link' :       str(link.split('/')[-1])
                      },
                    mode        =   self.city,
                    platform    =   self.platfrom or 'web',
                    proxy       =   self.proxy
                )
            )

    def join_channel_by_link(
        self: Client,
        link: str
        ) -> (dict):
        
        '''
        this method for join channel with link
        '''
        
        return (
                GetData.api(
                    version     =   self.api_version or '4',
                    auth        =   self.auth,
                    method      =   'joinChannelByLink',
                    data        =   {
                        'hash_link'     :   link.split('/')[-1]
                        },
                    mode        =   self.city,
                    platform    =   self.platfrom or 'android',
                    proxy       =   self.proxy
                )
            )