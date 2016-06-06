#! /usr/bin/python
'''
Created on May 30, 2016

@author: geiger
'''

from flask import Flask, make_response
from rory_view import Rory_view
from rory_model import Rory_Model
import json

class Rory(Flask):
    def __init__(self, name):
        Flask.__init__(self, name)
        self.model = Rory_Model()
        self.view = Rory_view(self.model)
        self.route_view()
        
    def route_view(self):
        view_routes = self.view.view_api() 
        for v_route in view_routes:
            self.add_url_rule(v_route['rule'], view_func=v_route['view_func'], methods=v_route['methods'])

api_router = Emily(__name__)
api_router.debug = True
#if __name__ == '__main__':
#    api_router.run(debug=True)

@api_router.errorhandler(404)
def not_found(error):
    return make_response(json.dumps({'error': 'Not found'}), 404)
    
#example of how to route
@api_router.route('/', methods=['GET'])
def index():
    return json.dumps([{'index': 'main'}, {'supported methods': 'GET'}, {'apidoc': '/apidoc'}])
