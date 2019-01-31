from nltk.tokenize import TweetTokenizer

import credentials_var as cred

results = cred.raw_collection.find()

for element in results:
    message = element["text"]
    tokens = TweetTokenizer().tokenize(message.lower())

    # Convert tokens as list to dictionary data type
    if not cred.tokens_collection.count_documents({"id_str": element["id_str"]}, limit=1) > 0:
        dictOfTokens = {str(i): tokens[i] for i in range(0, len(tokens))}
        dictOfTokens["id_str"] = element["id_str"]
        # Import dictOfTokens to mongodb
        cred.tokens_collection.insert_one(dictOfTokens)
