import mysql.connector
from mysql.connector import errorcode

def create_database():
    cursor = None
    connection = None

    try:
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "MySQL.Installer"
        )
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS book_store;")
        print("Database 'book_store' created successfully!")
    except mysql.connector.Error as e:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    finally:
        # Close the cursor and connection
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
create_database()