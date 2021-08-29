# Hotel_guestsDAO.py
# import the mysql connector module
import mysql.connector
# importing cursor from mysql connector
from mysql.connector import cursor
# importing dbconfig file that has my credentials for mysql
import dbconfig as cfg


# guestsDao class defined
class GuestsDAO:
    db = ""

    #def __init__(self):
    def connectToDB(self):
        self.db = mysql.connector.connect(
        host = cfg.mysql['host'],
        user = cfg.mysql['user'],
        password = cfg.mysql['password'],
        database = cfg.mysql['database']
        )
    
    #print("connection made")

    
    def __init__(self):
        self.connectToDB()            
    
    # Checking for connection, if none make one.
    def getCursor(self):
        if not self.db.is_connected():
            self.connectToDB()
        return self.db.cursor()

#################################################################################################################

    # function to create new data in a table
    def create(self, values):
        cursor = self.getCursor()
        
        sql = "insert into guest (guestID, guest_name, guest_surname, country) values (%s,%s,%s,%s)"
        
        cursor.execute(sql, values)
        self.db.commit()
        lastRowID = cursor.lastrowid
        cursor.close()
        return lastRowID
        

#################################################################################################################
   
    # function to get all data from table guest
    def getAll(self):
        cursor = self.getCursor()
        sql = "select * from guest"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDict(result))
        cursor.close()

        return returnArray
#################################################################################################################

    # function to find all data based on the entered id
    def findById(self, id):
        cursor = self.getCursor()
        sql = "select * from guest where id = %s"
        values = (id,) 
        cursor.execute(sql, values)
        result = cursor.fetchone()
        
        return self.convertToDict(result)
        #print(results)
 #################################################################################################################
        
    # function that updates all data based on entered id
    def update(self, values):
        cursor = self.getCursor()
        sql = "update guest set guestID =%s, guest_name =%s, guest_surname=%s, country=%s where id =%s"
    
        cursor.execute(sql, values)
        self.db.commit()
        #print("update done")
        

#################################################################################################################

    #function which deletes guest info based on entered id 
    def delete(self, id):
        cursor = self.getCursor()
        sql = "delete from guest where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        return {}
        
       
        
#################################################################################################################
    # function that converts the data from the database to JSON
    def convertToDict(self, result):
        colnames = ['id','guestID', 'guest_name', 'guest_surname', 'country']
        guest = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                guest[colName] = value
        return guest

# new instance of the guestDao class called
guestsDAO = GuestsDAO()