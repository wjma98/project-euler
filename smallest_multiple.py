# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 11:55:37 2020

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
        
#finds all prime factorization of a number as a list
def find_all_primes(n):
    primes = []
    for i in range(1, n+1):
        if is_prime(i) == True:
            primes.append(i)
    return primes

        
c = True
end = 15

list_prime = find_all_primes(end)
product = 1

number = 1 

for i in range(len(list_prime)-1):
    product *= list_prime[i]


while c:
    for i in range(1, end+1):
        if (product * number) % i != 0:
            break
        if i == end:
            print("Smallest number evenly divisible up to", end, "is", product * number)
            c = False
            break
    number += 1


    
    

 
