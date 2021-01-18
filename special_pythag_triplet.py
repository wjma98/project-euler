# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 00:24:55 2020

@author: William
"""


def find_triplet(end):
    for c in range(1,end):
        for b in range(1, c-1):
            for a in range(1, c-2):
                if (a*a+b*b == c*c and a+b+c==end):
                    print("a, b, c =", a,b,c)
                    print("product of the 3 = ", a*b*c)
                    return (a*b*c)

end = 1000
find_triplet(end)


            