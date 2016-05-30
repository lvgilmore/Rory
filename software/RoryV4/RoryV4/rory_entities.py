#! /usr/bin/python

from _ctypes import ArgumentError

class RoryHost():
    def __init__(self, hostname="", profiles=[],
                 alter_egos=[]):
        self.hostname = hostname
        self.profiles = profiles
        self.alter_egos = alter_egos 
        
class RoryProfile():
    def __init__(self, script= ""):
        self.script = script