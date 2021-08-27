  
# import the mysql connector module
import mysql.connector

from mysql.connector import cursor
import dbconfig as cfg


# hotel_guestsDao class defined
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
    

    def getCursor(self):
        if not self.db.is_connected():
            self.connectToDB()
        return self.db.cursor()

    # working create
    def create(self, values):
        cursor = self.getCursor()
        sql = "insert into guest (guestID, guest_name, guest_surname, country) values (%s,%s,%s,%s)"
        
            
       
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid


    # get method (working)...test code
    #returnValue = results = GuestsDAO().getAll()
    #print(returnValue)
    def getAll(self):
        cursor = self.getCursor()
        sql = "select * from guest"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        colnames=['id','guestID','guest_name', "guest_surname", "country"]
        #print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDict(result, colnames))

        return returnArray

    def findById(self, id):
        cursor = self.getCursor()
        sql = "select * from guest where id = %s"
        values = (id, ) 
        cursor.execute(sql, values)
        results = cursor.fetchone()
        colnames=['id', 'guestID', 'guest_name', 'guest_surname', 'country']
        return self.convertToDict(results, colnames)
        #print(results)
        
    # working
    def update(self, values):
        cursor = self.getCursor()
        sql = "update guest set guestID = %s, guest_name = %s, guest_surname=%s, country=%s where id = %s"
        
        cursor.execute(sql, values)
        self.db.commit()
        print("update done")
        cursor.close()
    #working
    def delete(self, guestID):
        cursor = self.getCursor()
        sql = "delete from guest where guestID = %s"
        values = [guestID]
        cursor.execute(sql, values)
        return {}
        
       
        

    def convertToDict(self, result, colnames):
        #colnames = ['id','guestID', 'guest_name', 'guest_surname', 'country']
        guest = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                guest[colName] = value
        return guest


guestsDAO = GuestsDAO()