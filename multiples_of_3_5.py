# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 19:46:23 2020

@author: William
"""
import numpy as np


sum = 0

end = 1000

for i in range(end):
    if (i % 3 == 0 or i % 5 == 0):
        print(i)
        sum +=i

print(sum)
        