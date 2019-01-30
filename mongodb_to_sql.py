import mysql.connector

import credentials_var as cred


# cursor = cred.coll.find({})
# for document in cursor:
#     print(document)


def db_create(dbname):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=""
    )

    dbCursor = mydb.cursor()
    dbCursor.execute("SHOW DATABASES")
    # Check if database already exists
    # dbExist = False
    for x in dbCursor:
        print(x)
        # f = open("database_list.txt", "w")
        # f.write(x)
        # if x == "('" + dbname + ",)":
        #     dbExist = True

    # if not dbExist:
    #     try:
    #         dbCursor.execute("CREATE DATABASE " + dbname)
    #     except:
    #         print("Error creating database")
    #     else:
    #         print("Database created")


# Check if table already exists
def table_create(dbname, tablename):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database=dbname
    )

    tableCursor = mydb.cursor()

    tableNotExist = True
    for x in tableCursor:
        if x == tablename:
            tableNotExist = False
        else:
            tableNotExist = True

    if tableNotExist == True:
        try:
            tableCursor.execute("CREATE TABLE " + tablename + " (name VARCHAR(255), address VARCHAR(255))")
        except:
            print("Error creating table")
        else:
            print("Table created")


dbname = "dbmantap"
tablename = "tabelmantap"

db_create(dbname)
# table_create(dbname, tablename)
