'''
Purpose: create a new database with the name "data.db"
         for storing data and a new table with the db-structure.
Note:    for editing data you can use SQLite data browser
Created on 20.06.2011
@author: Kamil Wozniak
'''

import sqlite3
import argparse
import Controller
import sys

if __name__ == '__main__':
    
    if len(sys.argv) < 2:
        print 'Use "-h" or "--help" to view the options.'
        
    parser = argparse.ArgumentParser(description='Setup configures the database connection.')
    parser.add_argument('--rmDev', action='store_true', help='removes all devices from the database')
    parser.add_argument('--rmData', action='store_true', help='removes all saved data from the database')
    parser.add_argument('--rmCMD', action='store_true', help='removes all saved CMD`s from the database')
    parser.add_argument('--sqlite3', action='store_true', help='creates a sqlite3 database called data.db in the same folder')
    parser.add_help
    
    args = parser.parse_args()
    ''' get the variables from namespace object '''
    argsArray = vars(args)  
    
    if argsArray['rmDev']:
        controller = Controller.Controller()
        controller.removeAllDevicesAction()
        print 'All devices removed.'
        
    if argsArray['rmData']:
        controller = Controller.Controller()
        controller.removeAllDataAction()
        print 'All data removed.'
        
    if argsArray['rmCMD']:
        controller = Controller.Controller()
        controller.removeAllCMDAction()
        print 'All CMD`s removed.'
    
    if argsArray['sqlite3']:
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
            
        cursor.execute("""CREATE TABLE data(
            id TEXT, value TEXT, read INTEGER, createdOn TEXT)""")
        
        cursor.execute("""CREATE TABLE devices(id TEXT)""")
        
        cursor.execute("""CREATE TABLE commands(id TEXT, cmd TEXT, 
                          read INTEGER, createdOn TEXT)""")
            
        connection.commit()
        connection.close()
        
        print("SQLite database has been created.")
    