# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 21:53:38 2020

@author: William
"""

input_a = [line.strip().split() for line in open('problem_18.txt')]  #this gives a 2d list of string elements
input_b = [line.strip().split() for line in open('problem_67.txt')]


matrix = [list(map(int, s)) for s in input_a]  #use list comprehension to turn string elements into int
matrix_2 =[list(map(int, s)) for s in input_b]

#This solution uses dynamic programming
def solution(array):
    for i in range(len(array)-2, -1, -1):
        for j in range(len(array[i])):
            array[i][j] += max(array[i+1][j], array[i+1][j+1])
    return array[0]
    
    
print(solution(matrix_2))

    
        