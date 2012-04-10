'''
Name: Controller
Purpose: Handle requests from the view and the wsn
Created on 22.06.2011
@author: Kamil Wozniak
'''
import DataRepository
from cmd import Cmd

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
        if wsnid:
            return self.dataRepository.readCMD(wsnid)
    
    '''
    Saves commands for a wsn id.
    This function should be used to control the wsns.
    '''
    def saveCMDAction(self, wsnid, cmd):
        if wsnid and cmd:
            self.dataRepository.saveCMD(wsnid, cmd)
    
    '''
    Clears the command-buffer (database) for all wsns.
    '''
    def removeAllCMDAction(self):
        self.dataRepository.removeAllCMD()
    
    '''
    This method should be used only by the SerialReader.
    The data form the connected device will be saved into the database.
    '''
    def saveDataAction(self, wsnid, value):
        if wsnid and value:
            self.dataRepository.saveData(wsnid, value)
        
    '''
    This method should be used only by the SerialReader. It stores the
    connected device in the database.
    '''
    def saveDeviceAction(self, wsnid, panid, channel):
        if id and panid and channel:
            self.dataRepository.saveDevice(wsnid, panid, channel)
    
    '''
    Returns a list of devices or nodes, which are currently connected
    to the host pc.
    '''
    def readDeviceList(self):
        return self.dataRepository.readDeviceList()
    
    '''
    Cleans all devices from the device table.
    '''
    def removeAllDevicesAction(self):
        self.dataRepository.removeAllDevices()
    
    '''
    Returns all data for a wsn id, no matter if the data was read
    before or not, like in "readLeatestAction".
    '''
    def readAllAction(self, wsnid):
        if wsnid:
            return self.dataRepository.readAllData(wsnid)
    
    '''
    Returns only unread data for a wsn id.
    '''
    def readLeatestAction(self, wsnid):
        if wsnid:
            self.dataRepository.readLeatestData(wsnid)
    
    '''
    Clears all stored "data" from the database.
    '''
    def removeAllDataAction(self):
        self.dataRepository.removeAllData()
        
    def __init__(self):
        '''
        Constructor
        '''
        self.dataRepository = DataRepository.DataRepository()
        