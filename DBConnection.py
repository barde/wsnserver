'''
Created on 09.10.2011
The sole purpose of this class is to return an
open database connection.
@author: Kamil Wozniak
'''
import sqlite3
import ConfigParser

try:
    import MySQLdb
    mysqlModExists = True
except ImportError:
    mysqlModExists = False

class DBConnection(object):
    
    '''
    Returns a database connection object, which can
    be used to execute SQL-code.
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
                
                conn = MySQLdb.connect(host, user, password, dbname)
                conn.text_factory = str
                return conn
    
    def __init__(self):
        '''
        Constructor
        '''  

        