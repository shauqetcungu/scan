
import pymysql

def show_databases():
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

        # SQL query string
        sqlQuery = "SHOW DATABASES"

        # Execute the sqlQuery
        cursorInstance.execute(sqlQuery)

        #Fetch all the rows
        databaseList = cursorInstance.fetchall()

        databases = []
        for database in databaseList:
            databases.append(database["Database"])
        return databases

    except Exception as e:
        print("Exception occurred:{}".format(e))
    finally:
        connectionInstance.close()