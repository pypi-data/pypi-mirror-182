#!/bin/python

from . import RubikaClient
from .client import ChannelMethods, GroupMethods, UserMethods


class Client(
    RubikaClient,
    UserMethods,
    GroupMethods,
    ChannelMethods
    ): # TODO: add all methods
    pass