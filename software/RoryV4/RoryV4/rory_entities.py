#! /usr/bin/python

from _ctypes import ArgumentError
from ipaddr import IPAddress
# from threading import Thread

class RoryAbstractHost():
    def __init__(self, ip=None, profiles=[]):
        if ip is None:
            raise ArgumentError("host must have an IP!")
        elif isinstance(ip, IPAddress):
            self.ip = ip
        elif isinstance(ip, str):
            self.ip = IPAddress(ip)
        else:
            raise ArgumentError("in RoryAbstractHost.__init__: ip: unknown class %s"
                                 % str(ip.__class__))
        self.profiles = profiles 
        
class RoryAbstractProfile():
    def __init__(self):
        pass
        
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