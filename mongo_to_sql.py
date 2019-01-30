import mysql.connector

import credentials_var as cred

sqldb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="dbmantap"
)

sqlCursor = sqldb.cursor()

mongoCursor = cred.coll.find({}, {"_id": 0, "id_str": 1, "text": 1})
for raw_data in mongoCursor:
    # print(raw_data["text"])

    # class FilteredData:
    #     def __init__(self, id_str, text):
    #         self.id_str = id_str
    #         self.text = text

    sql = "INSERT INTO tabelmantap (id, text) VALUES (%s, %s)"
    val = (raw_data["id_str"], raw_data["text"])
    sqlCursor.execute(sql, val)

    sqldb.commit()

    print(sqlCursor.rowcount, "record inserted.")
