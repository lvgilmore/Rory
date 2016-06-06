#! /usr/bin/python

'''
Created on Jun 06, 2016

@author: geiger
'''

import json
from rory_model import Rory_Model
from flask import request
from flask.helpers import make_response

class Rory_View():
    def __init__(self, model=None):
        if model is None: self.model = Rory_Model()
        else: self.model = model
        
    def hosts_api(self):
        try:
            if request.method == 'GET':
                make_response(json.dumps(self.model.get_hosts()), 200)
            elif request.method == 'POST':
                self.model.create_host(request_data(request))
                make_response(json.dumps(request_data(request)), 201)
            else:
                make_response(json.dumps({'message': "unknown method %s" % request.method,
                                          'location': "Rory_View.hosts_api"}),
                              400)
        except Exception as exc:
            make_response(json.dumps({'message': 'encountered exception',
                                     'location': "Rory_View.hosts_api",
                                     'details': exc}),
                          500)
    
    def host_api(self, host_id):
        try:
            if request.method == 'GET':
                make_response(json.dumps(self.model.get_host(host_id)), 200)
            elif request.method == 'PUT':
                self.model.update_host(request_data(request))
                make_response(json.dumps(request_data(request)), 201) 
            elif request.method == 'DELETE':
                if self.model.delete_host(host_id):
                    make_response(json.dumps(request_data(request)), 200)
                else:
                    make_response(json.dumps(request_data(request)), 404)
            else:
                make_response(json.dumps({'message': "unknown method %s" % request.method,
                                          'location': "Rory_View.host_api"}),
                              400)
        except Exception as exc:
            make_response(json.dumps({'message': 'encountered exception',
                                     'location': "Rory_View.host_api",
                                     'host_id': host_id,
                                     'details': exc}),
                          500)
    
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
    