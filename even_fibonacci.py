# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 19:51:08 2020

@author: William
"""

from functools import lru_cache

@lru_cache(maxsize=100)
#This function makes it such that python memorizes each value in the recursion function
#Without it, we have O(2^N) complexity, and it will take a very long time to compute

def fibbo(n):
    if n <= 1:
        return n
    else:
        return fibbo(n-2) + fibbo(n-1)


n = 0
sum = 0

while(fibbo(n) <= 4000000):
    if fibbo(n) % 2 == 0:
        sum += fibbo(n)
    n += 1

print(sum)
