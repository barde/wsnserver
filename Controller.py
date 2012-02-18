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
    Only the WSN should request this action
    ReadCMDAction looks into the database for new CMDs for a wsn id
    '''
    def readCMDAction(self, wsnid):
        self.dataRepository.readCMD(wsnid)
    
    '''
    Saved commands for a wsn id
    This function should be used to control the wsns
    '''
    def saveCMDAction(self, wsnid, cmd):
        self.dataRepository.saveCMD(wsnid, cmd)
    
    
    def removeAllCMDAction(self):
        self.dataRepository.removeAllCMD()
    
    def saveDataAction(self, wsnid, value):
        self.dataRepository.saveData(wsnid, value)
        
    def saveDevice(self, wsnid, panid, channel):
        if id and panid and channel:
            self.dataRepository.saveDevice(wsnid, panid, channel)
    
    def readDeviceList(self):
        return self.dataRepository.readDeviceList()
    
    def removeAllDevicesAction(self):
        self.dataRepository.removeAllDevices()
    
    ''' 
    Todo: Return value must be formated.
    '''
    def readAllAction(self, wsnid):
        return self.dataRepository.readAllData(wsnid)
    
    def readLeatestAction(self, wsnid):
        self.dataRepository.readLeatestData(wsnid)
    
    def removeAllDataAction(self):
        self.dataRepository.removeAllData()
        
    def __init__(self):
        '''
        Constructor
        '''
        self.dataRepository = DataRepository.DataRepository()
        