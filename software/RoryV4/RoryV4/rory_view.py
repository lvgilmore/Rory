#! /usr/bin/python

'''
Created on Jun 06, 2016

@author: geiger
'''

import json
from rory_model import Rory_Model

class Rory_View():
    def __init__(self, model=None):
        if model is None: self.model = Rory_Model()
        else: self.model = model
        
    def host_api(self):
        pass
    
    def view_api(self):
        routes = [
                {'rule': '/Rory/hosts',
                 'view_func': self.hosts_api,
                 'methods': ['GET', 'POST']},
                {'rule': '/Rory/hosts/<string:host_id>',
                 'view_func': self.host_api,
                 'methods': ['GET', 'PUT', 'DELETE']},
                {'rule': '/Rory/profiles',
                 'view_func': self.profiles_api,
                 'methods': ['GET', 'POST']},
                {'rule': '/Rory/profiles/<string:profile_id>',
                 'view_func': self.profile_api,
                 'methods': ['GET', 'DELETE']}
                ]
        return routes
    