import mysql.connector

#Creating a global variable
__cnx = None

def get_sql_connection():
    global __cnx
    #only initialise if the global variable is not initialized
    if __cnx == None:
        cnx = mysql.connector.connect(user='root', password='sirala',
                                          host='127.0.0.1',
                                          database='grocery_store')
    return cnx