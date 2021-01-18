# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 13:05:33 2020

@author: William
"""

def collatz_len(n):
    len = 0
    while n != 1:
        if n % 2 == 0:
            n = n/2
            len +=1
        else:
            n = 3*n+1
            len +=1
            
    return len
        

end = 1000000
longest_length = 0
num = 0

for i in range(1,end+1):
    print(i)
    if longest_length <= collatz_len(i):
        longest_length = collatz_len(i)
        num = i
        
print("longest collatz sequence under 1 million has length of ", longest_length)
print("number is", num)