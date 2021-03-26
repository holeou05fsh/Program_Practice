# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:59:43 2021

@author: ASUS
"""

a = int(input('input * amount:'))
b = input('To be increase input "+",To decrease input "-": ')

if b == '-' :
	for i in range(a,0,-1):
	    for c in range(0,i):
	        print('*',end='')
	    print()

	for n in range(0,a+1,1):
	    for c in range(0,n):
	        print('*',end='')
	    print()
	print('end')        
	
elif b == '+':
	for i in range(0,a+1,1):
	    for c in range(0,i):
	        print('*',end='')
	    print()

	for n in range(a+1,0,-1):
	    for c in range(0,n):
	        print('*',end='')
	    print()
	print('end')
else:
	print('input error')