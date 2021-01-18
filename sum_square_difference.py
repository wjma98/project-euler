# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 14:38:59 2020

@author: William
"""

def sum_of_squares(n):
    total = 0
    for i in range(1,n+1):
        total += i * i
    return total

def square_of_sum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    total *= total
    
    return total

n = 100
difference = square_of_sum(n) - sum_of_squares(n)

print("difference between squares of sum and sum of squares", difference)