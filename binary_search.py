# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 17:21:57 2019

@author: csmon
"""

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    while first <= last and not found:
      midpoint = (first + last)//2
      if alist[midpoint] == item:
         found = True
      else:
         if item < alist[midpoint]:
             last = midpoint-1
         else:
             first = midpoint+1
    return(midpoint)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42] # the lsit is in ascending order
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))