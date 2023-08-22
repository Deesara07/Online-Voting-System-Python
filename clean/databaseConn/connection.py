import mysql.connector

def create_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="voting"
    )
    return mydb
