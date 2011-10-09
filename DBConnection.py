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
        
    def getDBConnection(self):
        config = ConfigParser.RawConfigParser()
        config.read('wsn.cfg')
        
        type = config.get('Database-Config', 'type')
        
        if type == 'sqlite3':
            conn = sqlite3.connect("data.db")
            conn.text_factory = str
            return conn
        
        if type == 'mysql':
            return 0

    def __init__(self):
        '''
        Constructor
        '''  

        