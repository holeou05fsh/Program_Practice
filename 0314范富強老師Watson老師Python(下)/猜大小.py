# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 14:06:58 2021

@author: user
"""

import random

ans = random.randint(1,50)
guess = 0
while ans != guess:
    guess = int(input('輸入1~100之間整數猜數:'))
    if guess > ans:
        print("猜小一點")
    if guess < ans:
        print("猜大一點")
print("right")
