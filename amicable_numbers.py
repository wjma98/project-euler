# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 10:48:30 2021

@author: William
"""

def divisors(n):
    divisors = []
    for i in range(1,n):
        if n % i == 0:
            divisors.append(i)
    return divisors

end = 10000

# =============================================================================
# #For testing
# a = 220
# b = 284
# sum_a = sum(divisors(a))
# print(sum_a)
# print(sum(divisors(sum_a)))
# 
# =============================================================================

amicable_pairs = []
for i in range(1, end+1):
    n = sum(divisors(i))
    if i == sum(divisors(n)) and i != n:
        print(i, n, "are amicable pairs")
        amicable_pairs.append(i)
        amicable_pairs.append(n)
        

clean_list = []
[clean_list.append(x) for x in amicable_pairs if x not in clean_list]

print(clean_list)
print(sum(clean_list))

