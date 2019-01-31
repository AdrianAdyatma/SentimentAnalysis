from nltk.tokenize import TweetTokenizer
import mysql.connector

import credentials_var as cred

# sqldb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="",
#     database="dbmantap"
# )
#
# sqlCursor = sqldb.cursor()

results = cred.coll.find()

# list_results = tuple(results)

for element in results:
    message = element["text"]
    tokens = TweetTokenizer().tokenize(message.lower())
    print(type(tokens))

    # try:
    #     sql = "INSERT INTO tabeltoken (id_str, text) VALUES (%s, %s)"
    #     val = (raw_data["id_str"], tokens)
    #     sqlCursor.execute(sql, val)
    #
    #     sqldb.commit()
    # except:
    #     print("error inputing data to table sql", raw_data["id_str"])
    # else:
    #     print(sqlCursor.rowcount, "record inserted.")
