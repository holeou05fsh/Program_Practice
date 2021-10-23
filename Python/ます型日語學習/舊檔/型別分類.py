import re

with open('日語單字.txt','r',encoding='utf-8') as fp:
    lista = fp.read().splitlines()

masu_in = re.compile('\w+ます')
masu = []
for i in lista:
    if len(masu_in.findall(i))>0:
        masu.extend(masu_in.findall(i))
    else:
        pass
    
masu.sort()
with open('ます型單字(3字).txt','w',encoding='utf-8') as fp:
    for i in masu:
        if len(i) == 3:
            fp.write(i+'\n')


