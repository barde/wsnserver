'''
Purpose: create a new database with the name "data.db"
         for storing data and a new table with the db-structure.
Note:    for editing data you can use SQLite data browser
Created on 20.06.2011
@author: Kamil Wozniak
'''

import sqlite3
import argparse

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Setup configures the database connection.')
    parser.add_argument('--rmDev', action='store_true', help='removes all devices from the database')
    parser.add_argument('--rmData', action='store_true', help='removes all saved data from the database')
    parser.add_argument('--rmCMD', action='store_true', help='removes all saved CMD`s from the database')
    parser.add_help
    
    args = parser.parse_args()
    
    print args
    
    
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
        
    cursor.execute("""CREATE TABLE data(
        id TEXT, value TEXT, read INTEGER, createdOn TEXT)""")
    
    cursor.execute("""CREATE TABLE devices(id TEXT)""")
    
    cursor.execute("""CREATE TABLE commands(id TEXT, cmd TEXT, 
                      read INTEGER, createdOn TEXT)""")
        
    connection.commit()
    connection.close()
    
    print("Setup was successful. SQLite database has been created.")
    