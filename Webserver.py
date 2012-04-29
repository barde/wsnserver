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
        return "Command \"" + cmd + " \" was sent to target \"" + id + "\"." 
    
    @expose
    def readAll(self, id):
        controller = Controller.Controller()
        data = controller.readAllAction(id)
        
        ''' Encode the response into JSON '''
        string = "["
        for row in data:
            string += "{"
            string += "\"data\" : " + "\"" + row[1] + "\", "
            string += "\"createdOn\" : " + "\"" + row[3] + "\""
            string += "}"
            
            if row != data[len(data) - 1] :
                string += ","
        string += "]"
        return string
    
    @expose
    def readDeviceList(self):
        controller = Controller.Controller()
        devices = controller.readDeviceList()
        
        ''' Encode the response into JSON '''
        string = "["
        for row in devices:
            string += "{"
            string += "\"wsnid\" : " + "\"" + row[0] + "\", "
            string += "\"panid\" : " + "\"" + row[1] + "\", "
            string += "channel : " + "\"" + row[2] + "\""
            string += "}"
            
            if row != devices[len(devices) - 1] :
                string += ","
        string += "]"
        return string
    
    @expose
    def removeAll(self):
        controller = Controller.Controller()
        controller.removeAllDataAction()
        return "All messeges removed"

cherrypy.quickstart(Webserver())
#http://localhost:8080/index
        