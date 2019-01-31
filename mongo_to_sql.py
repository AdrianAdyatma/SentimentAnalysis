import mysql.connector

import credentials_var as cred

sqldb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="dbmantap"
)

sqlCursor = sqldb.cursor()

mongoCursor = cred.coll.find()

list_results = list(mongoCursor)
for raw_data in list_results:
    print(raw_data["user"]["screen_name"])

    # try:
    #     sql = "INSERT INTO tabelmantap (id_str, text) VALUES (%s, %s)"
    #     val = (raw_data["id_str"], raw_data["text"])
    #     sqlCursor.execute(sql, val)
    #
    #     sqldb.commit()
    # except:
    #     print("error inputing data to table sql", raw_data["id_str"])
    # else:
    #     print(sqlCursor.rowcount, "record inserted.")
