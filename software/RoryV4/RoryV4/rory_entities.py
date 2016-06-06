#! /usr/bin/python

from _ctypes import ArgumentError
from ipaddr import IPAddress
# from threading import Thread

class RoryAbstractHost():
    
    profiles = []
    
    def __init__(self, ip=None):
        if ip is None:
            raise ArgumentError("host must have an IP!")
        elif isinstance(ip, IPAddress):
            self.ip = ip
        elif isinstance(ip, str):
            self.ip = IPAddress(ip)
        else:
            raise ArgumentError("in RoryAbstractHost.__init__: ip: unknown class %s"
                                 % str(ip.__class__))
        
        # we set my_profiles as an empty array
        # then we check for each profile if it applies
        self.profiles = []
        for profile in RoryAbstractHost.profiles:
            if profile.am_i:
                self.profiles.append(profile)
    
    def self_search(self):
        pass
    
    def backend_config(self):
        pass
    
    def node_config(self):
        pass
        
class RoryAbstractProfile():
    def __init__(self, **kwargs):
        RoryAbstractHost.profiles.append(self)
        self.am_i = kwargs['am_i'] 
        
class RorySuperEgo():
    def __init__(self, alter_egos=[]):
        self.alter_egos = alter_egos
    
    def self_search(self):
        for ego in self.alter_egos:
            ego.self_search()
    
    def backend_conf(self):
        for ego in self.alter_egos:
            ego.backend_conf()
    
    def node_conf(self):
        for ego in self.alter_egos:
            ego.node_conf()