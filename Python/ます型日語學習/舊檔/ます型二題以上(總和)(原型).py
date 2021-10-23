import json
import re

with open('ます型二題以上(總和).json', 'r') as fp:
    a = json.load(fp)
    
single_list = [i for i in a.keys()]
# print(single_list)


with open('日語單字・ます.txt', 'r', encoding='utf-8') as fp:
    b = fp.read()  #lines
# b = [i.replace('\n','') for i in b]
# print(b)

li = []
for i in single_list:
    n = re.compile('\w+・'+i)
    # c += 1
    li.extend(n.findall(b))
    # 
# print(li)
key = re.compile('・\w+')
value = re.compile('\w+・')
dict = {}
for i in li:
    dict[value.findall(i)[0].replace('・',"")] = key.findall(i)[0].replace('・',"")
    
with open('ます型二題以上(總和)(原型).json', 'w') as fp:
    json.dump(dict, fp)
    
    

with open('ます型二題以上(總和)(原型).json', 'r',encoding='utf-8') as fp:
    pa = json.load(fp)
    
print(pa)
# l = [i for i in pa.values()]
# print(l)
    