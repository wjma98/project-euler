# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 23:52:38 2020

@author: William
"""

n = 1000
a =  2 ** n
str_a = str(a)


sum = 0
for i in range(len(str_a)):
    sum += int(str(str_a[i]))


print(sum)
               
               
             
    