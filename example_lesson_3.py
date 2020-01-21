# f=open('Документ.txt')
# wordlist = [f.read()]
# punclist = [".",";",":","!","?","/","\\",",","#","@","$","&",")","(","\""]
# for punc in punclist:
#     for word in wordlist:
#         wordlist=[word.replace(punc,'') for word in wordlist]
# a=word.split()
# print(wordlist)
# print(a)
# f.close()

f = open('Документ.txt')
content = f.read()
content = content.replace(".","").replace(",","").replace(";","").replace(":","").replace("!","").replace("?","").replace("/","").replace(")","").replace("(","").replace("-","").replace("«","").replace("»","").replace("—","")
lst = content.split()
lst_lower = list(map(lambda x: x.lower(), lst))
# print(lst_lower)

dct = {}
for word in lst_lower:
    if word in dct:
        dct[word] +=1
    else:
        dct[word] = 1
print(dct)