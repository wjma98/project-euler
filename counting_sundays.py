# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 09:57:04 2021

@author: William
"""

# September, April, June, and November = 30 days
# February = 28 or 29 if leap year
# The rest of the months = 31 days
# Leap year occurs any year divisble by 4, but not on century unless divisbible by 400
# 1 Jan 1900 was Monday, so 1 Jan 1901 starts on Tuesday

#First month is january and so on
months = [31, 28, 31, 30, 31, 30, 31 ,31 ,30 ,31 ,30 ,31]
days_week = ['Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

start_year = 1901
end_year = 2000

counter = 0

def leap_year(n):
    if n % 4 == 0 and n % 100 != 0:
        return True
    if n % 100 == 0 and n % 400 == 0:
        return True
    return False

def cumu_sum(array):
    array_2 = [x for x in array]
    print(array_2)
    for i in range(1, len(array_2)):
        array_2[i] += array_2[i-1]
    return array_2

#1901 starts on a Tuesday
start_day = 0 #Monday

for years in range(start_year, end_year+1):
    start_day += 1
    month_days = [i for i in months]
    days = 365
    if leap_year(years) == True:
        days += 1
        month_days[1] += 1
        print(years, "is leap year")
    if leap_year(years-1) == True and years % 4 == 1:   #Year after leap year starts two days after relative to previous year
        start_day +=1                                   #For example, 1904 starts on Friday, but 1905 starts on Sunday
    total_days = cumu_sum(month_days)
    start_of_month_days = [total_days[i] - month_days[i]+1 for i in range(len(total_days))]
    for days in range(1,days+1):
        if days == 1:
            print(days_week[(start_day+days-1)%7], years) #Prints first day of year
        if days in start_of_month_days and days_week[(start_day+days-1)%7] == 'Sunday':
            counter += 1
        
print("Sundays that appear in the first of month between years", start_year, "and", end_year, "is", counter)
    