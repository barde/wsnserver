'''
Name: DataRepository
Purpose: Handle database connections and communication
Created on 20.06.2011
@author: Kamil Wozniak
'''
import sqlite3

class DataRepository(object):
    
    def saveDevice(self, id):
        connection = self.__returnConnection()
        cursor = connection.cursor()
        
        cursor.execute("INSERT INTO devices VALUES (?)", [id])
        connection.commit()
    
    def readDeviceList(self):
        connection = self.__returnConnection()
        cursor = connection.cursor()
        
        cursor.execute("SELECT * FROM devices")
        devices = cursor.fetchall()
        connection.commit()
        return devices
    
    '''
    readCMD reads only the last cmd for a wsn id, sets all commands as read 
    '''
    def readCMD(self, id):
        connection = self.__returnConnection()
        cursor = connection.cursor()
        
        cursor.execute("SELECT * FROM commands WHERE id = ? AND read = 0 ORDER BY createdOn DESC LIMIT 1", [id])
        cmd = cursor.fetchall()
        cursor.execute("UPDATE commands set read = 1")
        connection.commit()
        return cmd
    
    def saveCMD(self, id, cmd):
        values = (id, cmd, False, sqlite3.datetime.datetime.now()) 
        sql = "INSERT INTO commands VALUES (?, ?, ?, ?)" 
        
        connection = self.__returnConnection()
        cursor = connection.cursor()
        cursor.execute(sql, values)
        connection.commit()
        
    def removeAllCMD(self):
        connection = self.__returnConnection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM commands")
        connection.commit()

    def removeAllData(self):
        connection = self.__returnConnection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM data")
        connection.commit()
    
    def readAllData(self, id):
        connection = self.__returnConnection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM data WHERE data.id = ?", [id])
        data = cursor.fetchall()
        cursor.execute("UPDATE data set read = 1")
        connection.commit()
        return data
    
    # not implemented yet
    def readLeatestData(self, id):
        connection = self.__returnConnection()
        cursor = connection.cursor()
        
        cursor.execute("SELECT * FROM data WHERE id = ? AND read = 0", [id])
        data = cursor.fetchall()
        cursor.execute("UPDATE data set read = 1")
        connection.commit()
        return data
    
    '''
    id: should contain the wsn-id
    value: should contain the data.
    '''
    def saveData(self, id, value):
        values = (id, value, False, sqlite3.datetime.datetime.now()) 
        sql = "INSERT INTO data VALUES (?, ?, ?, ?)" 
        
        connection = self.__returnConnection()
        cursor = connection.cursor()
        cursor.execute(sql, values)
        connection.commit()
        
    ''' 
    opens the database and returns the connection to work with
    '''
    def __returnConnection(self):
        return sqlite3.connect("data.db")

    def __init__(self):
        '''
        Constructor
        '''
        