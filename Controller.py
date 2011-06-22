'''
Created on 22.06.2011
@author: Kamil Wozniak
'''

class Controller(object):
    
    ''' 
    Only the WSN should request this action. 
    ReadCMDAction looks into the database for new CMDs
    '''
    def readCMDAction(self):
        pass
    
    def saveCMDAction(self):
        pass
    
    def readAllAction(self):
        pass
    
    def readLeatestAction(self):
        pass
    
    def removeAllAction(self):
        pass
        
    def __init__(self):
        '''
        Constructor
        '''
        