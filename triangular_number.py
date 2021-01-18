# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 03:39:20 2020

@author: William
"""


from functools import lru_cache

@lru_cache(maxsize=100)

def divisor(n):
    return set(
        factor for i in range(1, int(n**0.5) + 1) if n % i == 0
        for factor in (i, n//i)
    )



#the sum of n numbers
def triangular_number(n):
    if n == 1:
        return 1
    
    return n*(n+1)/2
    

n = 1
divisors = 500

while len((divisor(triangular_number(n)))) < divisors:
    n+=1
    
print("the smallest triangular number to have over", divisors, "divisors is n=", n) 
print("value of triangular number is", int(triangular_number(n)))
    
    


            