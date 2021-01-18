# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 11:06:41 2020

@author: William
"""



def check_pal(n):
    string = str(n)
    reversed_string = string[::-1]
    
    i = 0
    while i <= (len(string)-1):
        if string[i] != reversed_string[i]:
            return 0;
        else:
            if i == len(string)-1:
                return 1;
        i +=1
    
product = 0
greatest_pali = 0

factor_1 = 0
factor_2 = 0
# brute force all 3 digit multiplication
for a in range(100,1000):
    for b in range(100,1000):
        product = a * b
        if check_pal(product) == True:
            if greatest_pali <= product:   
               factor_1 = a
               factor_2 = b
               greatest_pali = product
            
            

print(greatest_pali)
print("factors are", factor_1, "and", factor_2)