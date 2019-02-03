import credentials_var as cred

file = open('kata-dasar-all.txt')

# def cutoff(string, pattern):
#    idx = string.find(pattern)
#    return string[:idx if idx != -1 else len(string)]

def formalize(word):
    for dict in file:
            if word == dict:
                return dict
            else:
                return word


# sent = input("Masukan Kalimat : ")
# print("Hasil : ", formalize(sent))

for tokens in cred.tokens_findAll:
    # print(type(tokens), len(tokens))
    for element in tokens:
        for token in range(len(tokens)-2):
            # print(tokens[str(token)]) #String
            token_ed = formalize(tokens[str(token)])
            print(token_ed)