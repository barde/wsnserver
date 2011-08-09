'''
Name: Webserver
Purpose: Handles requests from clients
Created on 21.06.2011
@author: Kamil Wozniak
'''

import Controller
import cherrypy
from cherrypy import expose

class Webserver:
    @expose
    def index(self):
        return "WSN-Server is up and running"
    
    @expose
    def sendCmd(self, id, cmd):
        controller = Controller.Controller()
        controller.saveCMDAction(id, cmd)
        return "Target: " + id + "<br>CMD: " + cmd
    
    @expose
    def readAll(self, id):
        controller = Controller.Controller()
        string = format(controller.readAllAction(id))
        return string
    
    @expose
    def removeAll(self):
        controller = Controller.Controller()
        controller.removeAllAction()
        return "All messeges removed"

cherrypy.quickstart(Webserver())
#http://localhost:8080/index
        