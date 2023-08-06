#!/bin/python

from . import (
    UserMethods,
    GroupMethods,
    ChannelMethods,
    )
from ..baseclient.main import RubikaClient

class Client(
    UserMethods.UserMethods,
    GroupMethods.GroupMethods,
    ChannelMethods.ChannelMethods,
    RubikaClient
    ): # TODO: add Socket or all methods
    pass