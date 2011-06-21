'''
Name: DataRepository
Purpose: Handle database connections and communication
Created on 20.06.2011
@author: Kamil Wozniak
'''
import sqlite3

class DataRepository(object):
    '''
    classdocs
    '''

    def removeAllFromDB(self):
        connection = self.__returnConnection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM data")
        connection.commit()
        
    # not impemented yet
    def removeFromDB(self):
        return True
    
    def readAllFromDB(self, createdBy):
        connection = self.__returnConnection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM data WHERE data.createdBy = ?", [createdBy])
        return cursor.fetchall()
        #connection.commit()
    
    # not implemented yet
    def readLeatestFromDB(self):
        return True
    
    '''
       type: can be "cmd" or "data"
       value: value can be the command or data
    '''
    def saveToDB(self, type, value, createdBy):
        values = (type, value, False, sqlite3.datetime.datetime.now(), createdBy) 
        sql = "INSERT INTO data VALUES (?, ?, ?, ?, ?)" 
        
        connection = self.__returnConnection()
        cursor = connection.cursor()
        cursor.execute(sql, values)
        connection.commit()
        
        
    ''' opens the database and returns the cursor to work with it '''
    def __returnConnection(self):
        return sqlite3.connect("data.db")

    def __init__(self):
        '''
        Constructor
        '''
        