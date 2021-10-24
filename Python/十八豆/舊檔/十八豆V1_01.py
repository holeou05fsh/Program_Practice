'''算同數字相加(玩法錯誤)'''

import random

for i in range(5):
	f = input('繼續(Y / N):')
	f = f.upper()
	if f == 'Y':
		a=random.randint(1,6)
		b=random.randint(1,6)
		c=random.randint(1,6)
		d=random.randint(1,6)
		print('[',end='')
		print(a,b,c,d ,sep=',' ,end=']\n')
		
		dice_1 = [a,b,c,d]
		dice_1a=set(dice_1)
		dice_1f = []
		for each1_a in dice_1a:
			count = 0
			for each1_b in dice_1:
				if each1_a == each1_b:
					count += 1
					if count == 4:
						dice_1f.append('青一色')
						dice_1f.append(each1_a)
					elif count == 3:
						dice_1f.append('三色')
					elif count == 2:
						dice_1f .append('一對')
						dice_1f.append(each1_a)
					elif count == 1:
						dice_1f.append('單')
						
		#print(dice_1f)
		
		if dice_1f.count('青一色') == 1 :
			print('青一色:',dice_1f[1])
		elif dice_1f.count('三色') == 1:
			print('在骰一次')
		elif dice_1f.count('一對') == 2:
			r = dice_1f.index('一對') + 1
			s = dice_1f.index('一對',r) + 1
			if dice_1f[r] > dice_1f[s]:
				print('數字:',dice_1f[1] * 2)
			else:
				print('數字:',dice_1f[3])
		elif dice_1f.count('一對') == 1:
			r = int(dice_1f.index('一對') ) + 1
			print('數字:',dice_1f[r] * 2)
		else:
			print('在骰一次')
	else:
		break