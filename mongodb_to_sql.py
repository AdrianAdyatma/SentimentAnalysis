import credentials_var as cred
import mysql.connector


# cursor = cred.coll.find({})
# for document in cursor:
#     print(document)


# MySQL Database identifier & connection
def db_check(self, dbname):
    self.dbname = dbname
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=""
    )
    dbCursor = mydb.cursor()

    # Check if database already exists
    dbNotExist = True
    for x in dbCursor:
        if x != dbname:
            dbNotExist = True

    if dbNotExist:
        try:
            dbCursor.execute("CREATE DATABASE " + dbname)
            print("Database created")
        except:
            print("Database exists")


# Check if table already exists
def table_check(self, dbname, tablename):

    self.dbname = dbname
    self.tableName = tablename
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database=dbname
    )

    tableCursor = mydb.cursor()

    tableNotExist = True

    tableCursor.execute("SHOW TABLES")

    for x in tableCursor:
        print(x)
