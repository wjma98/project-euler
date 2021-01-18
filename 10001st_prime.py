# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 14:45:57 2020

@author: William
"""

#checks if a number is prime
def is_prime(n):
    if n == 2 or n == 1:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
        else:
            if i == n-1:
                return True
        
nth_prime = 10001

n = []
a = 1

while len(n) <= nth_prime:
    if is_prime(a) == True:
        n.append(a)
    a += 1
    
print(nth_prime, "th prime digit is ", n[nth_prime])
    
    
