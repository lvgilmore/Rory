#! /usr/bin/python

from .rory_entities import RoryHost, RoryProfile

class RoryFSHost(RoryHost):
    pass

class RoryFSProfile(RoryProfile):
    pass

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