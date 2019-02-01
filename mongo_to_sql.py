
import credentials_var as cred

count = 0

list_results = list(cred.raw_findAll)
for element in list_results:
    # print(element["user"]["screen_name"])

    try:
        sql = "INSERT INTO tabelmantap (id_str, text) VALUES (%s, %s)"
        val = (element["id_str"], element["text"])
        # val = (element["id_str"], element["retweeted_status.extended_tweet.full_text"])
        cred.sqlCursor.execute(sql, val)

        # Commit all changes to sql
        cred.sqlDb.commit()
    except:
        print(element["id_str"], "export to sql error")
    else:
        print(element["id_str"], "export to sql success")
        count += 1

print(count, "data exported to sql")
