import json


with open('ます型題目(總和).json','r') as fp:
    a = json.load(fp)
# print(a)

li = [i for i in a.keys()]
num = 0
# print(a[li[n]])
n = {}
m = {}

for i in li:
    if len(a[i]) < 2:
        n[i] = a[i]
    else:
        m[i] = a[i]
    num += 1
# print(n)

with open('ます型題目不足(總和).json','w') as fp:
    json.dump(n, fp)

with open('ます型二題以上(總和).json','w') as fp:
    json.dump(m, fp)
    
#%%
    
# with open('ます型題目不足(總和).json','r') as fp:
#     a= json.load(fp)
#     print(len(a))
    
with open('ます型二題以上(總和).json','r') as fp:
    a= json.load(fp)
    print(len(a))