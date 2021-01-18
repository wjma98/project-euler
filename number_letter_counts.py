# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 23:56:28 2020

@author: William
"""

mydict = {0 : "" , 1 : "one", 2 : "two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", \
          8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen",14:'fourteen', 15:'fifteen', \
          16 : 'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen' , 20:"twenty", \
              30:"thirty", 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}


#counts total amount of characters used to write out 1 to 1000 in words
start = 1
end = 1000

total_letters = ''
for a in range(start, end+1):
    num = a
    str_num = str(num)
    
    
    digits = [int(i) for i in str_num]
    for i in range(len(digits)-1, -1, -1):
        digits[len(digits)-1-i] *= 10 ** i
    
    words = ''
    for i in range(len(digits)):
        
        #if 100, 200, 300, etc. dont want to add further words
        if num%100 == 0:
            if len(digits) == 4: 
                words += mydict[digits[i] // 10**(len(digits)-1)] +  ' thousand'
                total_letters += words
                break
        
            if len(digits) == 3:
                words += mydict[digits[i] // 10**(len(digits)-1)] + " hundred"
                total_letters += words
                break
        
        #if 1000
        if len(digits) == 4:
            words += mydict[digits[i] // 10**(len(digits)-1)] + ' thousand'
            continue
        
        #if it is a number like 345 where there is a middle number
        if len(digits) == 3 and i == 0:
            words += mydict[digits[i] // 10**(len(digits)-1)] + " hundred and "   
            continue
        
        #if need to use something like eleven... twenty since they are special
        if digits[i] == 10:
            words += mydict[digits[i] + digits[i+1]]
            total_letters += words
            break
        
        words += mydict[digits[i]]
        if i == len(digits)-1:
            total_letters += words
            #print("adding", words)

#print(words)
no_space = total_letters.replace(" ", "")
print("total characters from ", start, "to", end, "is =", len(no_space))


