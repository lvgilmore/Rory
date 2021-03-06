#! /usr/bin/python

from .rory_entities import RoryAbstractHost, RoryAbstractProfile

class RoryBasicHost(RoryAbstractHost):
    def __init__(self, hostname="", **kwargs):
        RoryAbstractHost.__init__(self, **kwargs)
        self.hostname = hostname
        
    def self_search(self):
        pass
    
    def backend_config(self):
        pass
    
    def node_config(self):
        pass
        
class RoryBasicProfile(RoryAbstractProfile):
    def __init__(self, script=""):
        self.script = script