'''
Created on 09.10.2011

@author: Kamil Wozniak
'''
import sqlite3

class DBConnection(object):
    '''
    classdocs
    '''
    
    def getDBConnection(self):
        return sqlite3.connect("data.db")

    def __init__(self):
        '''
        Constructor
        '''
        