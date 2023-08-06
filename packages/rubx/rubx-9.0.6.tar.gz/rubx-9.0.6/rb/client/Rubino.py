#!/bin/python

from random import randint

from requests import session as sn

from ..network import clients


class RubinoClient(
    clients,
    object):

    def __init__(
        self, session: str
        ) -> ...:
        self.session: sn = sn()
        self.auth: str = session

    def post(
        self,
        json: dict
        ) -> dict:
        for i in range(
            5
            ):
            with self.session.post(
                url=self.url,
                json=json
                ) as res:
                if res.status_code != 200:
                    continue
                else:
                    return res.json()
                    break
    
    def __enter__(
        self
        ) -> ...:
        return self

    def __exit__(
        self,
        *args,
        **kwargs
        ) -> ...: (
            ...
        )

    def makeJson(
        self,
        method: str,
        data: dict
        ) -> str:
        json: dict[str, ] = {
            'api_version':'0',
            'auth':self.auth,
            'client':self.client,
            'data':data,
            'method':method
            }
        return (
            json
            )

    def getProfileList(
        self,
        limit: int = 10,
        sort: str = 'FromMax',
        equal: bool = False
        ) -> dict:
        json = self.makeJson(
            'getProfileList',
            {
                'equal': equal,
                'limit':limit,
                'sort':sort,
                }
        )
        return self.post(
            json
            )

    def follow(
        self,
        followee_id: str,
        profile_id: str
        ) -> dict:
        json = self.makeJson(
            'requestFollow',
            {
            'f_type':'Follow',
            'followee_id':followee_id,
            'profile_id':profile_id
            }
            )
        return self.post(
            json=json
            )

    def unfollow(
        self,
        followee_id: str,
        profile_id: str
        ) -> dict:
        json = self.makeJson(
            'requestFollow',
            {
            'f_type':'Unfollow',
            'followee_id':followee_id,
            'profile_id':profile_id
            }
            )
        return self.post(
            json=json
            )

    def createPage(
        self, **kwargs
        ) -> dict:
        
        '''
        createPage(bio='', name='', username='', email='')
        '''
        
        json = self.makeJson(
            'createPage',
            {
                **kwargs
                }
            )
        return self.post(
            json=json
            )

    def updateProfile(
        self, **kwargs
        ) -> dict:
        ''' updateProfile(bio='', name='', username='', email='')'''
        json = self.makeJson(
            'updateProfile',
            {
                **kwargs
                }
            )
        return self.post(
            json=json
            )

    def isExistUsername(
        self,
        username: str
        ) -> dict:
        json = self.makeJson(
            'isExistUsername',
            {
            'username':username.replace('@','')
            }
            )
        return self.post(
            json=json
            )

    def getPostByShareLink(
        self,
        share_link: str,
        profile_id: str
        ) -> dict:
        json = self.makeJson(
            'getPostByShareLink',
            {
            'share_string':share_link,
            'profile_id':profile_id
            }
            )
        return self.post(
            json=json
            )

    def addComment(
        self,
        text: str,
        post_id: str,
        post_profile_id: str,
        profile_id: str
        ) -> dict:
        json = self.makeJson(
            'addComment',
            {
            'content':text,
            'post_id':post_id,
            'post_profile_id':post_profile_id,
            'rnd':randint(1111111111, 9999999999),
            'profile_id':profile_id
            }
            )
        return self.post(
            json=json
            )

    def likePostAction(
        self,
        post_id: str,
        post_profile_id: str,
        profile_id: str
        ) -> dict:
        json = self.makeJson(
            'likePostAction',
            {
            'action_type':'Like',
            'post_id':post_id,
            'post_profile_id':post_profile_id,
            'profile_id':profile_id
            }
            )
        return self.post(
            json=json
            )

    def unlike(
        self,
        post_id: str,
        post_profile_id: str,
        profile_id: str
        ) -> dict:
        json = self.makeJson(
            'likePostAction',
            {
            'action_type':'Unlike',
            'post_id':post_id,
            'post_profile_id':post_profile_id,
            'profile_id':profile_id
            }
            )
        return self.post(
            json=json
            )

    def addPostViewCount(
        self,
        post_id: str,
        post_profile_id: str
        ) -> dict:
        json = self.makeJson(
            'addPostViewCount',
            {
            'post_id':post_id,
            'post_profile_id':post_profile_id
            }
            )
        return self.post(
            json=json
            )

    def getComments(self,
        post_id: str,
        profile_id: str,
        post_profile_id: str,
        limit: int=50,
        sort: str='FromMax',
        equal: bool=False
        ) -> dict:
        json = self.makeJson(
            'getComments',
            {
            'equal':equal,
            'limit':limit,
            'sort':sort,
            'post_id':post_id,
            'profile_id':profile_id,
            'post_profile_id':post_profile_id
            }
            )
        return self.post(
            json=json
            )

    def getRecentFollowingPosts(self, profile_id: str, limit: int=30,
        sort: str='FromMax',
        equal: bool=False
        ) -> dict:
        json = self.makeJson(
            'getRecentFollowingPosts',
            {
            'equal':equal,
            'limit':limit,
            'sort':sort,
            'profile_id':profile_id
            }
            )
        return self.post(
            json=json
            )

    def getProfilePosts(self,
        target_profile_id: str,
        profile_id: str,
        limit: int=50,
        sort: str='FromMax',
        equal: bool=False
        ) -> dict:
        json = self.makeJson(
            'getRecentFollowingPosts',
            {
            'equal':equal,
            'limit':limit,
            'sort':sort,
            'profile_id':profile_id,
            'target_profile_id':target_profile_id
            }
            )
        return self.post(
            json=json
            )

    def getProfileStories(self,
                          target_profile_id: str,
                          limit: int = 100
                          ) -> dict:
        json = self.makeJson(
            'getProfileStories',
            {
            'limit':limit,
            'profile_id':target_profile_id
            }
            )
        return self.post(
            json=json
            )