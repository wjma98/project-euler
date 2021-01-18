# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 00:27:39 2021

@author: William
"""

def get_digits(n):
    digits = []
    while n >= 10:
        digits.append(n%10)
        n = n // 10
    digits.append(n)
    reverse_list = digits[::-1]
    return reverse_list



def factorial(n):
    if n==1:
        return n
    else:
        return n * factorial(n-1)


a = factorial(100)
print(sum(get_digits(a)))

