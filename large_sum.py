# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 04:28:30 2020

@author: William
"""

import numpy as np

digits = np.genfromtxt('problem_13.txt', dtype='str')

sum = 0

for i in range(len(digits)):
    sum += int(digits[i])
    
#print first 10 digits of sum
string = str(sum)
print("first 10 digits of sum is ", string[0:10])