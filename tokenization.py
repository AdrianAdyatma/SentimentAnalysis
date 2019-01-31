from nltk.tokenize import TweetTokenizer

import credentials_var as cred

# Read documents in raw tweets collection then export to mongodb
for element in cred.raw_findAll:
    message = element["text"]
    tokens = TweetTokenizer().tokenize(message.lower())

    # Check if tokens already inserted
    if not cred.tokens.count_documents({"id_str": element["id_str"]}, limit=1):

        # Convert tokens as list to dictionary data type
        dictOfTokens = {str(i): tokens[i] for i in range(0, len(tokens))}
        dictOfTokens["id_str"] = element["id_str"]

        # Export dictOfTokens to mongodb
        cred.tokens.insert_one(dictOfTokens)
        print(element["id_str"], "Export success")

    else:
        print(element["id_str"], "Already exported")
