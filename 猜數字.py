# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 14:00:49 2021

@author: ASUS
"""

import random
ans = random.randint(1,100)

guess = 0
min = 1
max = 100


while ans != guess:
	guess = int(input('input one num 1~100 : '))
	if guess <= min or guess >=max:
		print('I say ',min,'~',max,'! ok?')
	elif guess < ans:
		min = guess
		print(min,'~',max,' continue please')
	elif guess > ans:
		max = guess
		print(min,'~',max,' continue please')
	else:
		print('Congratulations, You have got it')
		