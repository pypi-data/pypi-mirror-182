#!/bin/python

from . import ChannelMethods, GroupMethods, UserMethods
from .main import RubikaClient


class Client(
    UserMethods.UserMethods,
    GroupMethods.GroupMethods,
    ChannelMethods.ChannelMethods,
    RubikaClient
    ): # TODO: add Socket or all methods
    pass