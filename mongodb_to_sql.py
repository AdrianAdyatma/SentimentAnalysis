import credentials_var as cred

cursor = cred.coll.find({})
for document in cursor:
    print(document)
