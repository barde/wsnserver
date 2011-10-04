'''
Name: Controller
Purpose: Handle requests from the view and the wsn
Created on 22.06.2011
@author: Kamil Wozniak
'''
import DataRepository

class Controller(object):
    
    ''' 
    Object for the dataRepository 
    '''
    dataRepository = 0
    
    ''' 
    Only the WSN should request this action. 
    ReadCMDAction looks into the database for new CMDs
    '''
    def readCMDAction(self, id):
        self.dataRepository.readCMD(id)
    
    def saveCMDAction(self, id, cmd):
        self.dataRepository.saveCMD(id, cmd)
        
    def removeAllCMDAction(self):
        self.dataRepository.removeAllCMD()
    
    def saveDataAction(self, id, value):
        self.dataRepository.saveData(id, value)
        
    def saveDevice(self, id):
        self.dataRepository.saveDevice(id)
    
    def readDeviceList(self):
        return self.dataRepository.readDeviceList()
    
    def removeAllDevicesAction(self):
        self.dataRepository.removeAllDevices()
    
    ''' 
    Todo: Return value must be formated.
    '''
    def readAllAction(self, id):
        return self.dataRepository.readAllData(id)
    
    def readLeatestAction(self, id):
        self.dataRepository.readLeatestData(id)
    
    def removeAllAction(self):
        self.dataRepository.removeAllData()
        
    def __init__(self):
        '''
        Constructor
        '''
        self.dataRepository = DataRepository.DataRepository()
        