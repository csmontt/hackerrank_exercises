# repeated string
# https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import math
import os
import random
import re
import sys

s = 'asd'
n = 1000000000000
n = 11

# Complete the repeatedString function below.
# inefficien way of doing it
def repeatedString(s, n):
    m = int(n/len(s))+1
    rep_s = s * m
    s_new = rep_s[0:n]
    n_aas = s_new. count('a')
    return(n_aas)

# In above solution i just repeat the string as many times as neccessary
# and then count the 'a', but if the string is too long i run out of memeory
# In fact, is not necessary to repeat the string at all.
    
# by diviing n by len of s we know how many times s fits in n. We canmultiply
# the number of 'a' in s by number of times len(s) fits in n. 
# But, we need to add the remaining 'a' in the remaining s.
# Instead of doing what I did, it would be simpler to use the % operator
# i woul dget the remaing characters in s, for which we should count the 
# number of 'a'
# and add them to c.
    
# efficient way of doing it
def repeatedString(s, n): 
    c = s.count('a') * (n//len(s))
    i = n - ((n//len(s))*len(s)) # could be replaced with this 
                                 # s[:n % len(s)]
    if (i != 0):
        new_s = s[0:i]
        c2 = new_s.count('a')
        c = c + c2
    return(c)
    
repeatedString(s, n)

# short code
# from https://www.hackerrank.com/rest/contests/master/challenges/repeated-string/hackers/victorz/download_solution?primary=true
def repeatedString(s, n): 
    return(s.count('a') * (n//len(s)) + s[:n % len(s)].count('a'))


