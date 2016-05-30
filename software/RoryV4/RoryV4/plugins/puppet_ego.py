#! /usr/bin/python

from .rory_entities import RoryHost, RoryProfile

class RoryPuppetHost(RoryHost):
    def __init__(self):
        self.ssl_public=""

class RoryPuppetProfile(RoryProfile):
    