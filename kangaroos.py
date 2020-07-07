#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/kangaroo/problem

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    x = x1
    v = x2
    i = 0
    while i <= 10000:
        x += v1
        v += v2
        i += 1
        print(i)
        if x == v:
            return("YES")
            break
        elif i == 10000:
            return("NO")


 
#https://www.mathblog.dk/hackerrank-kangaroo/
def kangaroo(x1, v1, x2, v2):
    #The case of same speed
    if v1 == v2 and x1 == x2:
        return 'YES'
    elif v1 == v2:
        return 'NO'
     
    x = (x2-x1) / (v1-v2)    
    if (x == round(x) and x > 0):
        return 'YES'
    else:
        return 'NO'
     
        
       
kangaroo(0,3,4,2) # yes

kangaroo(0,2,5,3)   # should be no!
        
kangaroo(14, 4, 98, 2) # yes

kangaroo(0, 2, 5, 3) # no