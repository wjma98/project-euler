# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 12:05:17 2021

@author: William
"""

def factors(n):
    results = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            results.update([i,int(n/i)])
    
    #delete last element since we dont want n in factor list
    divisors = sorted(list(results))
    del divisors[-1]
    return divisors

def abundant_number(n):
    if sum(factors(n)) > n:
        return True
    else:
        return False
    
# Credit to StackOverflow post, https://stackoverflow.com/questions/11792708/generate-all-possible-combinations-from-a-int-list-under-a-limit
# User Lauritz V. Thaulow
# Finds all possible sums of a list below the limit
def sums(lst, limit):
    from itertools import combinations_with_replacement
    p = set(x + y for x, y in combinations_with_replacement(lst, 2)) 
    return sorted([x for x in p if x <= limit])

# 12 is smallest abundant number
# 28123 is the biggest interger than can be written as sum of 2 abudant number
end = 28123
all_abund_numbers = []
for i in range(1, end+1):
    if abundant_number(i) == True:
        all_abund_numbers.append(i)

all_pairs = sums(all_abund_numbers, end)

unique =[x for x in range(1, end+1) if x not in all_pairs]
print(sum(unique))
        
