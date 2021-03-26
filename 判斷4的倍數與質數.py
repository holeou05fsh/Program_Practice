# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:55:25 2021

@author: ASUS
"""

n = int(input('input num:'))

if n % 4 == 0:
 print(n,'is 4 multiple')
else:
 print(n,'is not 4 multiple')

a = 2

for i in range(2, n):
 if n % a == 0:
  print('not prime number')
  break
 a += 1

if n == a:
 print('is prime number')
