'''
Name: Webserver
Purpose: Handles requests from clients
Created on 21.06.2011
@author: Kamil Wozniak
'''

import cherrypy
from cherrypy import expose

class Webserver:
    @expose
    def index(self):
        return "Hello World!"

cherrypy.quickstart(Webserver())
#http://localhost:8080/celc_to_fahr?degrees=50
        