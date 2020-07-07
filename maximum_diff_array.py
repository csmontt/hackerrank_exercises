# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:09:27 2019

@author: csmon
"""

# Maximum difference in an array

# You are given an array of integers and you have to compute
# the maximum difference between any item and any lower indexed smaller
# item for all the possible pairs, i.e., for a given array a find the maximum
# value of a[j] - a[i] for all i,j, where 0 <= i <= j < n and a[i] < a[j]. If
# there are no lower indexed smaller items for all items, then return -1.

# For example, given an array [1,2,6,4], you would first compare 2 to the 
# elements to its left. 1 is smaller so calculate the difference 2-1 =1. 6
# is bigger than 2 and 1, so calculate the differences 4 and 5. 4 is only bigger
# than 2 and 1, and the differences are 2 and 3. The largest difference was
# 6 - 1= 5

#def maxDifference(n, a):
    #dsfs
#    return 

a = [7, 9, 5, 6, 3, 2]
b =[1,2,6,4]
c = [6,5,2]

# Supposely this solution uses 'dynamic programming'.
# instead of using max(a) or any other function that needs
# to iterate over the list. We just update the minvalue
# and maxdifference with a for loop. Therefore we are not
# stroing any data on another list neither.

def maxDiff(a):
    vmin = a[0] # set minimum value to first element of array
    dmax = 0 # start max difference as 0
    for i in range(len(a)): # iterate over every element in the list
        #print(a[i], vmin, dmax)
        if (a[i] < vmin): # we don´t care about the difference between the current
            vmin = a[i]   # value of a an every previous element, just the smaller
        elif (a[i] - vmin > dmax): # we the maximum difference we have seen so far 
            dmax = a[i] - vmin
        #print(a[i], vmin, dmax)
    if dmax == 0:
        return -1
    else:
        return dmax
    
maxDiff(a)
maxDiff(b)
maxDiff(c)

# modify the code to consider the difference between any element in the array
# this is quite easy using already made functions
def maxDiff2(a):
    return max(a)-min(a)
    
maxDiff2(a)

# try without those predefined functions
def maxDiff3(a):
    biggest = a[0]
    smallest = a[0]
    for i in range(len(a)):
        print(biggest, smallest)
        if (a[i] > biggest):
            biggest = a[i]
        elif (a[i] < smallest):
            smallest = a[i]  
    return(biggest - smallest)
            
maxDiff3(a)

# modify code so only difference between the iest number and the reamining
# integers to its right are considered.
# solution a) reveerse the list and don´t change anything

def reverseElms(a):
    revList = []
    for i in range(len(a)):
        revList.append(a[(len(a)-1)-i])
    return revList

def maxDiff4(a):
    a = reverseElms(a)
    vmin = a[0]
    dmax = 0 
    for i in range(len(a)):
        if (a[i] < vmin): 
            vmin = a[i]  
        elif (a[i] - vmin > dmax):  
            dmax = a[i] - vmin
    if dmax == 0:
        return -1
    else:
        return dmax
    
maxDiff4(a)

# Do the same but without the help of reverse
# dont sure if it works for every case,
# I just changeg the greater than and less than signs.
def maxDiff5(a):
    vmin = a[0]
    dmax = 0 
    for i in range(len(a)):
        if (a[i] > vmin): 
            vmin = a[i]  
        elif (a[i] - vmin < dmax):  
            dmax = a[i] - vmin
    if dmax == 0:
        return -1
    else:
        return abs(dmax)
    
maxDiff5(a)
