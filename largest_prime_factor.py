# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 22:19:19 2020

@author: William
"""


def find_prime(n):
    factors = []
    duplicate = []
    i = 1
    
    number = n
    
    #find all factors
    while i <= number:
        if n % i == 0:
            factors.append(i)
            number /= i
        i +=1
    
    duplicate.extend(factors)
    
    #find prime factors and replace non-prime with 1's in list
    for x in range(len(factors)):
        i = 2
        while i <= factors[x]-1:
            if factors[x] % i == 0:
                print("removing", factors[x], "with i = ", i)
                factors.pop(x)
                factors.append(1)
                continue
            i +=1
    
    prime_factors = []
    
    #remove duplicates
    for x in factors:
        if x in duplicate:
          duplicate.remove(x)
          prime_factors.append(x)
    
    return prime_factors

#n = 13195 
n = 600851475143 
print(find_prime(n))