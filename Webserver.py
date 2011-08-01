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
        return "WSN-Server is up and running"
    
    @expose
    def sendCmd(self, target, cmd):
        return "Target: " + target + "<br>CMD: " + cmd
    
    @expose
    def readAll(self):
        return "Here are all messeges from the db"
    
    @expose
    def removeAll(self):
        return "All messeges removed"

cherrypy.quickstart(Webserver())
#http://localhost:8080/index
        