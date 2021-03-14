# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 15:54:48 2021

@author: user
"""

fruits = ['apple','banana','orange','charry','orange']
n = fruits.index('orange') #index只能找list內有的東西,index只找第一個
print(n)

v = fruits.count('orange')  #count 數數量
print(v)


print('='*20) #===================


name = input('輸入水果:')

if fruits.count(name) !=0:
    print('{}在索引值:{}'.format(name,fruits.index(name)))
else:
    print('找不到')


print('='*20) #===================


name = input('輸入水果:')

index = 0
if fruits.count(name) !=0:
    for i in range(n):
        index = fruits.index(name,index)
        print(index)
        index += 1
else:
    print('找不到')

