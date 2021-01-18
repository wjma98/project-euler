# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 11:50:46 2020

@author: William
"""

# =============================================================================
# 
# #find all the primes below a certain number
# #not fast enough
# def find_prime(n):
#     primes = []
#     
#     if n == 1:
#         primes.append(1)
#     
#     if n>=2:
#         primes.append(1)
#         primes.append(2)
#         
#     x = 1
#     for i in range(3,n):
#         for x in range(2,i):
#             if x == i-1:
#                 primes.append(i)
# 
#             if i % x == 0:
#                 break
#     
#     return primes
# 
# =============================================================================

#sieve's algorithm for primes
#faster
def find_prime(n):
    primes = [True for i in range(n)]
    prime_numbers = []
    
    p = 2
    while p*p <= n :
       if primes[p] == True:
            for i in range(2*p, n, p):
                primes[i] = False
       p +=1 
    
    primes[0] = False
    primes[1] = False
    
    for p in range(1,n):
        if primes[p] == True:
            prime_numbers.append(p)
            
    
    return prime_numbers


n = 2000000
print("sum of primes below,", n, "is ", sum(find_prime(n)))
        
    
    
    

            
            
            