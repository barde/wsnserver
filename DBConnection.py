'''
Created on 09.10.2011

@author: Kamil Wozniak
'''
import sqlite3
import ConfigParser
import sys

try:
    import MySQLdb
    mysqlModExists = True
except ImportError:
    mysqlModExists = False

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
            if mysqlModExists == False:
                print('MySQLdb module can not be found. Read the README.txt')
            else:
                host = config.get('Database-Config', 'host')
                user = config.get('Database-Config', 'user')
                password = config.get('Database-Config', 'password')
                dbname = config.get('Database-Config', 'dbname')
                
                return MySQLdb.connect(host, user, password, dbname)
    
    def __init__(self):
        '''
        Constructor
        '''  

        