  
# import the mysql connector module
import mysql.connector

from mysql.connector import cursor 


# hotel_guestsDao class defined
class GuestsDAO:
    db = ""

    def __init__(self): 
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hotel_guests"
        )
        #print("connection made")


    

    def getCursor(self):
        if not self.db.is_connected():
            self.connectToDB()
        return self.db.cursor()

    # working create
    def create(self, guest):
        cursor = self.getCursor()
        sql = "insert into guest (guestID, guest_name, guest_surname, country) values (%s,%s,%s,%s)"
        values = [
            guest['guestID'],
            guest['guest_name'],
            guest['guest_surname'],
            guest['country']
            
        ]
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
        #print(results)
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append()

        return returnArray

    def findById(self, guestID):
        cursor = self.getCursor()
        sql = "select * from guest where guestID = %s"
        values = ['guestID']
        cursor.execute(sql, values)
        results = cursor.fetchone()
        return self.covertToDict(results)
        #print(results)
        
    # working
    def update(self, guest):
        cursor = self.getCursor()
        sql = "update guest set guest_name = %s, guest_surname=%s, country=%s where guestID = %s"
        values = [
            guest['guest_name'],
            guest['guest_surname'],
            guest['country'],
            guest['guestID']
            
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return guest
    #working
    def delete(self, guestID):
        cursor = self.getCursor()
        sql = "delete from guest where guestID = %s"
        values = [guestID]
        cursor.execute(sql, values)
        return {}
        
       
        

    def covertToDict(self, result):
        colnames = ['guestID', 'guest_name', 'guest_surname', 'country']
        guest = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                guest[colName] = value
        return guest


guestsDAO = GuestsDAO()