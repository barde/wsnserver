'''
Name: DataRepository
Purpose: Handle database connections and communication
Created on 20.06.2011
@author: Kamil Wozniak
'''
import sqlite3
import DBConnection

class DataRepository(object):
    
    '''
    Saves the device id to the database
    '''
    def saveDevice(self, id):
        connection = self.__returnConnection()
        cursor = connection.cursor()
        
        cursor.execute("INSERT INTO devices VALUES (?)", [id])
        connection.commit()
    
    '''
    Returns the devices known to the system
    '''
    def readDeviceList(self):
        connection = self.__returnConnection()        
        cursor = connection.cursor()
        
        cursor.execute("SELECT id FROM devices")
        
        devices = []
        for row in cursor:
            devices.append(row[0])
        
        connection.commit()        
        return devices
    
    '''
    readCMD reads only the last cmd for a wsn id, sets all commands as read 
    '''
    def readCMD(self, id):
        connection = self.__returnConnection()
        cursor = connection.cursor()
        
        cursor.execute("SELECT cmd FROM commands WHERE id = ? AND read = 0 ORDER BY createdOn DESC LIMIT 1", [id])
        
        cmd = ''
        for row in cursor:
            cmd = row[0]
            
        cursor.execute("UPDATE commands set read = 1 WHERE id = ?", [id])
        connection.commit()
        return cmd
    
    '''
    Save a command for a wsn
    '''
    def saveCMD(self, id, cmd):
        values = (id, cmd, False, sqlite3.datetime.datetime.now()) 
        sql = "INSERT INTO commands VALUES (?, ?, ?, ?)" 
        
        connection = self.__returnConnection()
        cursor = connection.cursor()
        cursor.execute(sql, values)
        connection.commit()
        
    '''
    Removes all commands from the database
    '''
    def removeAllCMD(self):
        connection = self.__returnConnection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM commands")
        connection.commit()
    
    '''
    Removes all devices from the database
    '''
    def removeAllDevices(self):
        connection = self.__returnConnection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM devices")
        connection.commit()

    '''
    Removes all data from the database
    '''
    def removeAllData(self):
        connection = self.__returnConnection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM data")
        connection.commit()
    
    '''
    Return the all collected data for a wsn
    '''
    def readAllData(self, id):
        connection = self.__returnConnection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM data WHERE data.id = ?", [id])
        data = cursor.fetchall()
        cursor.execute("UPDATE data set read = 1")
        connection.commit()
        return data
    
    '''
    Return the unread data for a wsn
    '''
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
        return DBConnection.DBConnection().__getDBConnection()

    def __init__(self):
        '''
        Constructor
        '''
        