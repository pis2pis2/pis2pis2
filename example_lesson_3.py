f=open('Документ.txt')
wordlist = [f.read()]
punclist = [".",";",":","!","?","/","\\",",","#","@","$","&",")","(","\""]
for punc in punclist:
    for word in wordlist:
        wordlist=[word.replace(punc,'') for word in wordlist]
a=word.split()
print(wordlist)
print(a)
f.close()

# f=open('Документ.txt')
# content=f.read()
# puncList = [".",";",":","!","?","/","\\",",","#","@","$","&",")","(","\""]
# for word in content:
#     content=content.replace('punc','')
# print(content)
#
# a='2'
# print(a,type(a))
# b=list(a)
# print(b,type(b))
# c=str(b)
# print(c,type(c))