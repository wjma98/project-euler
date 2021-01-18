# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 11:22:20 2021

@author: William
"""


# Maps 'A' to the interger 1 and so on
def char_to_num(n):
    return ord(n) - 64

file = open('problem_22.txt').read()
names = file.split(",")

# Take away the quotes in string
for index,item in enumerate(names):
    names[index] = item.strip('"')
    
names = sorted(names)

name_total = 0
name_score = 0

for i in range(len(names)):
    name_score = 0
    for j in range(len(names[i])):
        name_score += char_to_num(names[i][j])
        if j == len(names[i])-1:
            name_total += (i+1) * name_score
        
print(name_total)
