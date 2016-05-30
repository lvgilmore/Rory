#! /usr/bin/python

from .rory_entities import RoryAbstractHost, RoryAbstractProfile
from time import sleep

class RoryPuppetHost(RoryAbstractHost):
    def __init__(self, ssl_public="", puppet_master=None,
                 hostgroup="", **kwargs):
        RoryAbstractHost.__init__(self, **kwargs)
        self.ssl_public = ssl_public
        self.puppet_master = puppet_master
        self.hostgroup = hostgroup

class RoryPuppetProfile(RoryAbstractProfile):
    def __init__(self, configgroups=[], **kwargs):
        RoryAbstractProfile.__init__(self, **kwargs)
        self.configgroups = configgroups