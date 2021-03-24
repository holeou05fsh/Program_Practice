'''
由系統亂數產生1~49之間，6個不重複的整數，請遞增排序印出
'''

import random
num = []
while True:
	a = random.randint(1,100)
	if len(num)>=6:
		break
	if num.count(a) == 0:
		num.append(a)
print(num)

num.sort(reverse = False)
print(num)