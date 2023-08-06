#!/bin/python

from . import ChannelMethods, GroupMethods, UserMethods
from .main import RubikaClient


class Client(
    RubikaClient,
    UserMethods.UserMethods,
    GroupMethods.GroupMethods,
    ChannelMethods.ChannelMethods
    ): # TODO: add all methods
    pass