
import pymysql
import datetime

def create_database(newDatabaseName):
    # Create a connection object
    databaseServerIP            = "127.0.0.1"  # IP address of the MySQL database server
    databaseUserName            = "root"       # User name of the database server
    databaseUserPassword        = ""           # Password for the database user

    charSet                     = "utf8mb4"     # Character set
    cursorType                  = pymysql.cursors.DictCursor

    connectionInstance = pymysql.connect(host=databaseServerIP, user=databaseUserName, password=databaseUserPassword,charset=charSet,cursorclass=cursorType)

    try:

        # Create a cursor object
        cursorInstance  = connectionInstance.cursor()

        # SQL Statement to create a database
        sqlStatement = "CREATE DATABASE "+ newDatabaseName

        # Execute the create database SQL statement through the cursor instance
        cursorInstance.execute(sqlStatement)

    except Exception as e:
        print("Exeception occured:{}".format(e))
    finally:
        connectionInstance.close()