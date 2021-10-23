import random
import json

with open('ます型題目(總和).json','r') as fp:
    a = json.load(fp)
    

li = [i for i in a.keys()]
list_num = random.randint(0,len(li))

while len(a[li[list_num]]) < 2:
    list_num = random.randint(0,len(li))

x = li[list_num]
# print(x)

question = a[x]

question_num = random.randint(0, len(question)-1)
q = question[question_num]
L = random.sample(range(0, 4), 4)

li_num = random.sample(range(0, len(li)), 3)
while list_num in li_num:
    li_num = random.sample(range(0, len(li)), 3)

list =[x,li[li_num[0]],li[li_num[1]],li[li_num[2]]]
dic = {'A':list[L[0]],'B':list[L[1]],'C':list[L[2]],'D':list[L[3]]}
# print(dic['A'])
Q = q.replace(x,'_'*len(x))
print(Q)
print('A.{}  B.{}  C.{}  D.{}'.format(dic['A'],dic['B'],dic['C'],dic['D']))
try:
    if x == dic[input('答案：').upper()]:
        print('正確 O')
    else:
        print('錯誤 X')
        print("正確答案:",x)
except:
    print('輸入錯誤')
