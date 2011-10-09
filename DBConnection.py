'''
Created on 09.10.2011

@author: Kamil Wozniak
'''
import sqlite3
import ConfigParser

class DBConnection(object):
    '''
    classdocs
    '''
    
    type = None
    
    def getDBConnection(self):
        if self.type == 'sqlite3':
            conn = sqlite3.connect("data.db")
            conn.text_factory = str
            return conn

    def __init__(self):
        '''
        Constructor
        '''  
        config = ConfigParser.RawConfigParser()
        config.read('wsn.cfg')
        
        self.type = config.get('Database-Config', 'type')
        