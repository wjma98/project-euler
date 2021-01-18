# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 13:27:43 2020

@author: William
"""

#where n is the nxn grid 


from itertools import permutations 
from scipy.special import comb

#This works, but only for small paths. Too inefficient since computing (2*n)! is very taxing and large
def num_paths(n):
    unique_paths = []
    moves = n*'N' + n*'E'
    #print(moves)
    possible = permutations(moves)
    
    for item in possible:
        if (item not in unique_paths):
            unique_paths.append(item)
    
    return len(unique_paths)
    

n = 20

#Analytical solution - the number of paths going from the (0,0) to (n,n) in a nxn grid is given by
# 2*n choose n since there are 2*n steps total steps and n is the steps to go up/right
k = comb(n*2, n)

print("grid size of", n)
print("number of possibe paths are ", int(k))