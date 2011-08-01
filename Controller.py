'''
Created on 22.06.2011
@author: Kamil Wozniak
'''
import DataRepository

class Controller(object):
    
    ''' Object for the dataRepository '''
    dataRepository = 0
    
    ''' 
    Only the WSN should request this action. 
    ReadCMDAction looks into the database for new CMDs
    '''
    def readCMDAction(self):
        pass
    
    def saveCMDAction(self):
        pass
    
    def saveDataAction(self, id, value):
        self.dataRepository.saveData(id, value)
    
    ''' Return value must be implemented (formated).'''
    def readAllAction(self, id):
        return self.dataRepository.readAllData(id)
    
    def readLeatestAction(self):
        pass
    
    def removeAllAction(self):
        self.dataRepository.removeAllData()
        
    def __init__(self):
        '''
        Constructor
        '''
        self.dataRepository = DataRepository.DataRepository()
        