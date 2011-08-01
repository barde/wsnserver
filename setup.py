'''
Purpose: create a new database with the name "data.db"
         for storing data and a new table with the db-structure.
Note:    for editing data you can use SQLite data browser
Created on 20.06.2011
@author: Kamil Wozniak
'''

import sqlite3

if __name__ == '__main__':
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()
        
    cursor.execute("""CREATE TABLE data(
        id TEXT, value TEXT, read INTEGER, createdOn TEXT)""")
    
    cursor.execute("""CREATE TABLE devices(id TEXT)""")
    
    cursor.execute("""CREATE TABLE commands(id TEXT, cmd TEXT, createdOn TEXT)""")
        
    connection.commit()
    connection.close()
    
    print("Setup was successful.")
    