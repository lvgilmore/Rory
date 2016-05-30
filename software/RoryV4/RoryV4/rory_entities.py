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
                
class FileSystem():
    def __init__(self, mountpoint, vg="",
                 size=5, options="defaults",
                 source=None, lvname="",
                 fstype='xfs'):
        self.mountpoint = str(mountpoint)
        if source is None:
            if vg == "": vg = "VolumeGroup-01"
            self.vg = vg
            self.fstype = fstype
            if lv == "":
                self.lv = self.mountpoint[1:].replace('/', '-') + "-lv"
            else:
                self.lv = lv
            
        elif vg == "":
            self.source = source
            self.fstype = 'nfs'
            
        else:
            raise ArgumentError("FS cannot be both NFS and local..")