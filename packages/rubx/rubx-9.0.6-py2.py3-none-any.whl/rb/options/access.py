#!/bin/python

class Accesses(object):
    
    class Admin(str):
        (
            PinMessages,
            setAdmin,
            ChangeInfo,
            BanMember,
            SetJoinLink,
            SetMemberAccess,
            DeleteGlobalAllMessages
            ) = (
                'PinMessages',
                'setAdmin',
                'ChangeInfo',
                'BanMember',
                'SetJoinLink',
                'SetMemberAccess',
                'DeleteGlobalAllMessages'
                )
    class User(str):
        (
            ViewMembers,
            ViewAdmins,
            SendMessages,
            AddMember
            ) = (
                'ViewMembers',
                'ViewAdmins',
                'SendMessages',
                'AddMember'
                )