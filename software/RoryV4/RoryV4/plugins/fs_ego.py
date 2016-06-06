#! /usr/bin/python

from .rory_entities import RoryAbstractHost, RoryAbstractProfile
from commands import getstatusoutput

class RoryFSHost(RoryAbstractHost):
    def __init__(self, primary_vg="fedora", **kwargs):
        RoryAbstractHost.__init__(self, **kwargs)
        self.primary_vg = primary_vg
    
    def self_serach(self):
        candidates = getstatusoutput("ssh root@" + str(self.ip) + " 'vgs --noheadings'")
    
    def self_search(self):
        pass
    
    def backend_config(self):
        pass
    
    def node_config(self):
        pass
        

class RoryFSProfile(RoryAbstractProfile):
    def __init__(self, fss=[], **kwargs):
        RoryAbstractProfile.__init__(self, **kwargs)
        self.fss = fss

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