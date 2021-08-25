  
# import the mysql connector module
import mysql.connector
# import the dbconfig.py file which contains my credentials to log into mysql
import dbconfig as cfg

# bull class defined
class Hotel_guestsDAO:
    db=""

    # function to connect to the database, connection pooling added
    def initConnectToDB(self):
        db = mysql.connector.connect(
            host=       cfg.mysql['host'],
            user=       cfg.mysql['user'],
            password=   cfg.mysql['password'],
            database=   cfg.mysql['database'],
            pool_name='my_connection_pool',
            pool_size=10
        )
        return db
        # testing
        print("connection made")

   