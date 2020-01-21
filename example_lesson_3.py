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

import pymorphy2
morph = pymorphy2.MorphAnalyzer()
lst_morph = []
for word in lst_lower:
    p = morph.parse(word)[0]
    lst_morph.append(p.normal_form)

lst_diff = set(lst_morph)

dct = {}
for word in lst_morph:
    if word in dct:
        dct[word] +=1
    else:
        dct[word] = 1
print(dct)

print ('5 наиболее часто встречающихся слов:')
lst_srt = sorted(dct.items(), key=lambda x: x[1],reverse=True)
for i in range(5):
    print(lst_srt[i][0],'-',lst_srt[i][1])
print('Количество разных слов в тексте: ', len(lst_diff))