# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 13:57:21 2020

@author: William
"""


import numpy as np

matrix = np.loadtxt('problem_11_matrix.txt')


#index j moves horizontally
#index a moves vertically

def down(n, step, j,a):
    product = 1
    for i in range(step):
        if (i+a) >= len(n):
             return 0
        #print(n[i+a][j], ", i = ", i, ",j =", j)
        product *= n[i+a][j] 
    
    return product
    

def right(n,step, j, a):
    product = 1
    for i in range(step):
        if i+a >= len(n):
            return 0
        #print(n[j][i+a], ", i = ", i, ",j =", j)
        product *= n[j][i+a]
    return product

def left_diagnol(n, step, j, a):
    product = 1
    for i in range(step):
        if i+a >= len(n) or i+j >= len(n):
            return 0
        #print(n[i+a][i+j], ", i = ", i, ",j =", j)
        product *=n[i+a][i+j]
    return product


def right_diagnol(n, step, j, a):
    product = 1
    for i in range(step):
        if 3+a-i >= len(n) or i+j >= len(n):
            return 0
        #print(n[3+a-i][i+j], ", i = ", i, ",j =", j)
        product *=n[3+a-i][i+j]
    return product
    

step = 4
#print(down(matrix, step, 15, 6))
#print(right(matrix,step, 15, 6))
#print(left_diagnol(matrix, step, 15, 6))
#print(right_diagnol(matrix, step, 0,1))

greatest_product = 0

for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(i,j)
        if greatest_product <= max(down(matrix,step,i,j), right(matrix,step,i,j), \
                                   left_diagnol(matrix,step,i,j), right_diagnol(matrix,step,i,j)):
            greatest_product = max(down(matrix,step,i,j), right(matrix,step,i,j), \
                                   left_diagnol(matrix,step,i,j), right_diagnol(matrix,step,i,j))
    
            print("max is at i = ", i, ",j = ", j)

print(int(greatest_product))

    




    