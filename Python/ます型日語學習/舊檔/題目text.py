import random

a = '東日本大震災'
q = '1.東日本大震災で多くの人が亡くなった2011年のあと、9年続けて長くなっています。'
L = random.sample(range(0, 4), 4)
list =['東日本大震災','西日本大震災','南日本大震災','北日本大震災']
dic = {'A':list[L[0]],'B':list[L[1]],'C':list[L[2]],'D':list[L[3]]}
print(dic['A'])
Q = q.replace(a,'_'*len(a))
print(Q)
print('A.{}  B.{}  C.{}  D.{}'.format(dic['A'],dic['B'],dic['C'],dic['D']))
if a == dic[input('答案：').upper()]:
    print('正確')
else:
    print('錯誤')