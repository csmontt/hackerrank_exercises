# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 17:13:43 2019

@author: csmon
"""
import numpy as np
array = [1,2,3]


aa = [5,6,7]
bb = [3,6,10]

def points(a, b):
    score_a = 0
    score_b = 0
    for i in range(len(a)):
        if aa[i] - bb[i] > 0:
            score_a += 1
        elif aa[i] - bb[i] < 0:
            score_b += 1
    return([score_a, score_b])

def compareTriplets(a, b):
    res_a = []
    res_b = []
    for i in range(len(a)):
        dif = a[i] - b[i]
        if dif > 0:
            res_a.append(1)
            res_b.append(0)
        elif dif < 0:
            res_a.append(0)
            res_b.append(1)
        else:
            res_a.append(0)
            res_b.append(0)
    return([sum(res_a), sum(res_b)])  

# Given a square matrix, calculate the absolute 
# difference between the sums of its diagonals.


matrix = [['A', 'B', 'C', 'D', 'E'], ['A', 'B', 'C', 'D', 'E'], ['A', 'B', 'C', 'D', 'E'], ['A', 'B', 'C', 'D', 'E'], ['A', 'B', 'C', 'D', 'E']]
for row in matrix:
  print(' '.join(row))
  
square_m = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

#def sumMat(mat):
#    diag_1 = []
#    diag_2 = []
#    for i in range(len(mat)):
#        diag_1.append(mat[i][i])
#        diag_2.append(mat[i][len(mat)-1-i])
#    return(sum(diag_1, diag_2))
    
def sumMat(mat):
    diag_1 = 0
    diag_2 = 0
    for i in range(len(mat)):
        diag_1 += mat[i][i]
        diag_2 += mat[i][len(mat)-1-i]
    return(abs(diag_1 - diag_2))
  
# Given an array of integers, calculate the fractions of its 
# elements that are positive, negative, and are zeros. Print 
# the decimal value of each fraction on a new line.

sample = [-4,3,-9,0,4,1]  
def plusMinus(arr):
    res = []
    # positive
    res.append(len([item for item in arr if item > 0])/len(arr))
    # negative
    res.append(len([item for item in arr if item < 0])/len(arr))
    # 0s
    res.append(len([item for item in arr if item == 0])/len(arr))   
    for element in res:
        print("%0.06f" %element)
        
# Consider a staircase of size :

   #
  ##
 ###
####
# Observe that its base and height are both equal to , and 
# the image is drawn using # symbols and spaces. The last 
# line is not preceded by any spaces.

# Write a program that prints a staircase of size n.

def staircase(n):
    for i in range(n):
        hashes = '#'*(i+1)
        print(hashes.rjust(n))
        


# Given five positive integers, find the minimum and maximum 
# values that can be calculated by summing exactly four of the
#  five integers. Then print the respective minimum and maximum
#  values as a single line of two space-separated long integers.

# For example, arr = [1,3,5,7,9]. Our minimum sum is 16 and our 
# maximum sum is 24. We would print
# 16 24        

arr1 = [233,34,34,3,5]
def miniMaxSum(arr):   
    max_sum = sum([item for item in arr if item != min(arr)])
    min_sum = sum([item for item in arr if item != max(arr)])
    print(min_sum, max_sum)

arr2 = [5, 5, 5, 5, 5] 
def miniMaxSum2(arr):     
    min_val = [item for item in arr if item == min(arr)][0]
    max_val = [item for item in arr if item == max(arr)][0]
    print(sum(arr)-max_val, sum(arr)-min_val)

miniMaxSum2(arr1)
miniMaxSum2(arr2)

# You are in charge of the cake for your niece's birthday and 
# have decided the cake will have one candle for each year of 
# her total age. When she blows out the candles, she’ll only 
# be able to blow out the tallest ones. Your task is to find 
# out how many candles she can successfully blow out.

# For example, if your niece is turning  years old, and 
# the cake will have  candles of height , , , , she will
# be able to blow out  candles successfully, since the 
# tallest candles are of height  and there are  such candles.

import time

ar1 = [9999999]*10000

# using list comprehension
def birthdayCakeCandles(ar): 
    candles = len([item for item in ar if item == max(ar)])
    return(candles)
    
start = time.time()
birthdayCakeCandles(ar1)
end = time.time()
print(end - start)

# using for loop
def birthdayCakeCandles2(ar):
    count=0
    big = max(ar)
    for i in range(len(ar)):
        if(ar[i]==big):
            count+=1
    return count

%timeit len([item for item in ar1 if item == max(ar1)])

# using a generator

%timeit birthdayCakeCandles2(ar1)


def birthdayCakeCandles3(ar):
    return sum(x == max(ar) for x in ar)
# return sum(1 for x in ar if x==max(ar))

start = time.time()
birthdayCakeCandles3(ar1)
end = time.time()
print(end - start)

def birthdayCakeCandles4(ar):
    return ar.count(max(ar))

start = time.time()
birthdayCakeCandles4(ar1)
end = time.time()
print(end - start)

%timeit birthdayCakeCandles4(ar1)

    
# convert time to 24 hour clock time-------------------------------------------
# 07:05:45PM to 19:05:45
times1 = "07:05:45PM"
times2 = "12:00:00AM"
times3 = "12:00:00PM"

# weird that with strings indices don´t start at 0, not the case,
# is just that if I put two it actually goes uo to 1!
str(int(newstr[:2])+12) + newstr[2:8]

def timeConversion(s):
    if s.find('AM') != -1 and int(s[:2]) == 12:
        time = s.replace('AM', '')
        time = time.replace('12', '00')
        return time
    elif s.find('AM') != -1:
        time = s.replace('AM', '')
        return time
    elif s.find('PM') != -1 and int(s[:2]) == 12:
        time = s.replace('PM', '')
        return time
    else:
        time = s.replace('PM', '')
        return str(int(s[:2])+12) + s[2:8]
    
timeConversion(times)

# another way
def timeConversion(s):
    t = s.rstrip('APM').split(':') 
    t[0] = int(t[0]) 
    t[0] = t[0] % 12 
    if s.find('PM') != -1: 
        t[0] += 12 
        t[0] = str(t[0]) 
        s = ':'.join(t) 
        return(s)
    else:
        s = ':'.join(t)
        return(s)
    
print(timeConversion(times1))   
print(timeConversion(times2)) # doen workd
print(timeConversion(times3))


# another way, but doesnt convert 12am to 00!
h, m, s = map(int, times2[:-2].split(':'))
p = times[-2:]
h = h % 12 + (p.upper() == 'PM') * 12
print(('%02d:%02d:%02d') % (h, m, s))


# Xor-sequence ----------------------------------------------------------------
# given an array and left and right indices I need to get the Xor sum
# of x-1 to x for x > 0.
# For example, A = [0,1,3,0,4,1,7,0,8]. The segment from l = 1 and r = 4
# sum to 1 xor 3 xor 0 xor 4 = 6.
# see https://www.tutorialspoint.com/python/bitwise_operators_example.htm


A = [0,1,3,0,4,1,7,0,8,1,11,0,12,1,15,0] #,16,1,19,0,20,1,23,0,24,1]

# I need an Array as input but it can be done without one!
def xorSum(l, r):
    sumxor = A[l]
    for i in range(l+1,r+1):
      sumxor = sumxor^A[i]
    return(sumxor)
    
print(xorSum(1,2))
print(xorSum(2,3))
print(xorSum(3,4))
print(xorSum(4,5))
print(xorSum(5,6))

print(xorSum(3,6))
print(xorSum(5,6))
        
# Without Array!
def xorSequence(l,r):
    X = lambda i: [i, 2, i+2, 0][(i%8)//2] # // is the floored-division 
                                           # operator in Python.
    return(X(r) ^ X(l-1))
    
# It's a straight forward O(1) solution based on the following
#  properties of XOR and A:
# Ai = 0 ⊕ 1 ⊕ ... ⊕ i, for all i ≥ 0.
# Define the sequence X as Xi = A0 ⊕ A1 ⊕ ... ⊕ Ai. 
# Its first 16 terms are: 0, 1, 2, 2, 6, 7, 0, 0, 8, 9, 2, 2, 14, 15, 0, 0. 
# This sequence has the following pattern: Xi is equal to
# i, if r = 0
# 2, if r = 1
# i+2, if r = 2
# 0, if r = 3 
# where r = (i mod 8) / 2 Como mierda se le ocurrio esto?
# If x ⊕ y = z, then y ⊕ z = x, z ⊕ x = y and x ⊕ y ⊕ z = 0.
# Properties 1 and 2 have been used in line 1 of the code and 
# property 3 in line 4.


# Sum vs XOR ------------------------------------------------------------------
# other way

# got it from https://blog.angularindepth.com/the-simple-math-behind-decimal-binary-conversion-algorithms-d30c967c9724    
def intTobin(num):
    binN = []
    while num > 0:
        remainder = num%2  # didnt worked when this was after num = num//2
        num = num//2
        binN.append(str(remainder)) 
    binN = list(reversed(binN))
    return(''.join(binN))
    
    
def sumXor(n):
    return(2**(intTobin(n).count('0')) if bool(n) else 1)
    
def sumXor(n):
    return(2**(format(n, 'b').count('0')) if bool(n) else 1)
     
# example n = 4
(4 + 0) == (4^0) # True
(4 + 1) == (4^1) # True
(4 + 2) == (4^2) # True
(4 + 3) == (4^3) # True
    
# example n = 3
format(3, 'b')  
intTobin(3)
# binary representation of 3 is 11, it has
# no zeros in it  
format(3, 'b').count('0')
# though, we can see that for any number, at least
# the first case e.g. for 3
(3 + 0) == (3^0) # True
# therefore, for any number, at least 
#  n + 0 = n ^ 0 is true.
2**(format(3, 'b').count('0'))
# the above gives 1.
# now, I don´t know how people got to this logic but 2 to the power
# of zeros in the binary representation of a number gives the number of
# times the sum of n + from 0 to n-1 == n^n-1 (not the best formulation
# i know but at least I should get it in the future).
# The if n else 1 part, is added to deal with special cases
# when n is 0 and because of it it returns 1 instead of 2.
# When n = 0, format(0, 'b').count('0') is 1, therefore 
# 2**1 is two instead of 1, which is waht we want.

    
# my way that takes too long!
def sumXor(n):
    counter = 0
    if n == 0:
        n = 1
    for i in range(0,n):
        counter = counter + int(n + i == n^i)
    return(counter)



# Climbing the Leaderboard ----------------------------------------------------

scores = [50, 100, 100, 40, 40, 20, 10]
alice = [5, 25, 50, 120]

# takes too long for large arrays
# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alices):
    # ocupé el algoritmo the binarySearch
    # http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBinarySearch.html
    def binarySearch(alist, item):
        first = 0 # indice del priemr elemento
        last = len(alist)-1 # indice del último elemento
        found = False # si fue o no encontrado el item
        while first <= last and not found:
            # meintras first sea < o igual last y aún
            # no ha sido encontrado el elemento
            # calcular el midpoint del array
            midpoint = (first + last)//2
            # si el elemento en el midpoint
            # es igual a l item, el item 
            # fu encontrado y el midpoint corresponde
            # al indice de donde se encuentra el item
            if alist[midpoint] == item:
               found = True
            else:
            # si item no es encontrado y item es 
            # menor al número en el midpoint del array
            # last se convierte en el midpoint -1
                if item < alist[midpoint]:
                   last = midpoint-1
            # otherwise last no cambia pero si cambia
            # first, que ahora seria el midpoint + 1
            # así, nos deshacemos de la mitad que queda del
            # array.
                else:
                   first = midpoint+1
        return(midpoint)
    # inicio list pa guardar el ranking de cada score de alice
    rank_alice = []
    for i in range(len(alice)):
        # añado a los scores el score iesimo de alice
        score_i = scores +  alice[i:i+1]
        # dejo sólo los scores únicos y los ordeno de menor a mayor
        # porque el algoritmo de binary search que ocupe funcionaba
        # para ese caso, podría tratar de cambiarlo.
        unique_scores = sorted(set(score_i))
        # obtener el índice del score iesimo de alice en la lista
        # de score que contiene ese número.
        rank_alice.append(len(unique_scores) - binarySearch(unique_scores, 
                          alice[i]))
    return(rank_alice)  
    
# It's not quite THE way to do it. Binary search is not needed 
# because Alice's scores are strictly ascending. You only need 
# to start at the bottom of the leaderboard and move up as necessary.
# This changes the complexity from O(n+m*log(n)) to O(n+m) and 
# the code is even simpler.
            
# getting the rank of each value, was suppose to be part
# of another function to get the rank of each alice score
    rank = [1]
    for i in range(len(scores)-1):
        if (scores[i] == scores[i+1]):
            rank.append(rank[i])
        else:
            rank.append(rank[i]+1)
    score_rank = list(zip(scores, rank))


# Works perfectly!
# obtained dfrom hackerrank
def climbingLeaderboard(scores, alices):
    unique_scores = list(reversed(sorted(set(scores))))
    i = len(alice)-1
    j = 0
    ans = []
    while i >= 0:
        if j >= len(unique_scores) or unique_scores[j] <= alice[i]:
            ans.append(j+1)
            i -= 1
        else:
            j += 1
    return reversed(ans)
%timeit climbingLeaderboard(scores, alice)


# another way, it takes even less time
def climbingLeaderboard(scores, alice):
    # este weon obtiene los resultados únicos primero
    scores_set = list(set(scores))
    # luego los ordena de mayor a menor
    scores_set.sort(reverse=True)
    # crea lista para guardar resultados
    result = []
    # obtiene el largo de la lista de scores.
    l = len(scores_set)
    # para cada score de alice
    for s in alice:
        # mientras l es mayor a 0 y s es mayor igual
        # al último elemento de la lista de scores
        # le sustraemos 1 a l.
        while (l>0) and (s >= scores_set[l-1]):
            l -= 1
        # el while loop termina cuando s es igual
        # o mayor al último elemento actual de scores
        # cuando eso sucede, ese es el resultado para el
        # elemento s de alice. Y lo guardamos en results.
        # Le sumamos 1, porque en el paso anterior le restamos 
        # 1?
        result.append(l+1)
    return result
       
%timeit climbingLeaderboard(scores, alice)

# iteración 1 for loop
# alice = [5, 25, 50, 120]
# example above if s = 5
# iteracion 1 while loop
# while (5>0) and (5 >= 10):
# result.append(5+1)
# results = [6]

# iteración 2 for loop
# s is 25 now and l is still 5.
# while (5>0) and (25 >= 10):
#   5 -= 1
# while (4>0) and (25 >= 20):
#   4 -= 1
# while (3>0) and (25 >= 40):
# result.append(3+1)  
# results = [6,4]

# iteración 3 for loop
# s is 50 now and l is 3.
# while (3>0) and (50 >= 40):
#   3 -= 1
# while (2>0) and (50 >= 50):
#   2 -= 1
# while (1>0) and (50 >= 100):
# result.append(1+1)  
# results = [6,4,2]

# iteración 4 for loop
# s is 120 now and l is 1.
# while (1>0) and (120 >= 100):
#   1 -= 1
# while (0>0) and (120 >= scores_set[0-1]): # aunque se cumple segunda
# condición, no se cumple la priemra asíq que el loop para.
# result.append(0+1)  
# results = [6,4,2,1] 
# ?


# The hurdle race--------------------------------------------------------------

jump = 4
heights = [1, 6, 3, 5, 2]

def hurdleRace(k, height):
    if max(height)-k <= 0:
        return(0)
    else:
        return(max(height)-k)

res1 = hurdleRace(jump, heights)

def hurdleRace(k, height):
    return max(height) - k if k < max(height) else 0 

res2 = hurdleRace(jump, heights)

# Designer PDF Viewer---------------------------------------------------------

letters = 'abc'
heights = [1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]

# mine takes less time than the one below 
def designerPdfViewer(h, word): 
    list_height = []
    for w in list(word):
        list_height.append(h[ord(w) - ord('a')]) # ord('a') = 97 
    return max(list_height)*len(word)

%timeit designerPdfViewer(heights, letters)


def designerPdfViewer(h, word): 
    word = [heights[ord(c)-ord('a')] for c in list(word)]
    return(max(word)*len(word))
    
%timeit designerPdfViewer(heights, letters)    

# utopian tree ----------------------------------------------------------------
# when n[i] is odd we multiply the height of the tree
# by 2 when is pair we add 1
def utopianTree(n):
    h = 1
    for i in range(n):
       if (i+1)%2 !=0:
           h = h * 2
       else:
           h = h + 1
    return h

# Angry professor -------------------------------------------------------------
a = [0 ,-1,2,1]
k = 2

def angryProfessor(k, a):
    if len([assist for assist in a if assist <= 0]) < k:
        return('YES') # class is cancelled
    else:
        return('NO')
        
# beautifulDays ---------------------------------------------------------------
# https://stackoverflow.com/questions/14763722/python-modulo-on-floats
        
import re
import math
i = 1
j = 123456   
k = 13


def beautifulDays(i, j, k):
    beautiful = 0
    for i in range(i,j+1):
        s = ''.join(reversed(str(i)))
        num = (abs(i - float(s)))/k
        if num.is_integer():
            beautiful += 1
    return beautiful

beautifulDays(i, j, k)        

# i[::-1] same as ''.join(reversed(str(i)


# Viral advertising -----------------------------------------------------------
def viralAdvertising(n):
    cumulative = 0
    shared = 5
    for i in range(1,n+1):
      liked = shared//2
      cumulative += liked
      shared = liked*3
    return cumulative
        
# Save the prisonner ----------------------------------------------------------
# for n prisoners m candies are given in sucession, the giving
# starts at prisoner s. If m candies are given to n prisoners and the
# the giving starts at prisoner s, determine which is the last prisoner 
# to receive a candy.

# My way
# I imagined we had to use modulo operator, the same as we use when
# when we try to determine the time in a wall clock.
# for example, the wall clock goes from 1 to 12 if we receive 16, the mod
# result from 16%12 = 4, which is indeed the time in the wall clock.

# here, I took the number of candies % number of prisoners and add to it
# s - 1, -1 otherwise the count starts in position 1 instead of 0?
# to that we took % n. Following the example of the clock, if we add a number
# and is larger than the hours in the clock, we need to take the modulo to 
# know in whcih position ends up.
# if the result is == 0, it means that the last prisoner got the candy.
# cause the n%n == 0.
# otherwise whe function is the same.
def saveThePrisoner(n, m, s):
    if ((m%n + s-1) % n) == 0:
        return n
    else:
      return ((m%n + s-1) % n) 


# Shorter way
def saveThePrisoner(n, m, s):
     return ((m+s-2)%n)+1   
 
# explanation
# So, I can do my best, I think I understand what is going on here.
# Assuming we started counting the prisoners from 0, like most 
# arrays, we could just print the result of: 
# (startingPrisoner - 1 + candies ) % numPrisoners

# The % keeps the index in bounds [0, numPrisoners) and 
# the minus one to the startingPrisoner accounts for the fact 
# the first prisoner eats the candy and we want to return their 
# position and not the next prisoner's position. I hope this makes sense.

# Because this problem uses 1 as the first "index" so to 
# speak for the prisoners, we want to add one after the result 
# of the remainder operator. But, if we do this, most things will 
# be skewed by one, so we balance adding the one to the remainder 
# by taking one away from the dividend. Check this:

# 6 % 5 = 1
# 6 % 5 + 1 = 2 (obviously not equal to the above)
#(6 - 1) % 5 + 1 = 1

# (startingPrisoner - 1 - 1 + candies ) % numPrisoners + 1

# Subtracting an additional one from the dividend and 
# adding a one to the remainder allows our math to still work out the same as:

# (startingPrisoner - 1 + candies ) % numPrisoners

# except, it won't allow a value of 0 and will allow numPrisoners
#  to result as well, resulting in a range of: [1, numPrisoners]

# Hopefully this helps.
    
# Circular Array Rotation------------------------------------------------------
a = [1,2,3]
k = 2
queries = [0,1,2]

def circularArrayRotation(a, k, queries):
    newArray = []
    for i in range(len(a)):
       newArray.append(a[(len(a) - (k % len(a))+i)%len(a)])
    return(list(map(lambda i: newArray[i], queries)))  

def circularArrayRotation2(a, k, queries):
    return [a[((len(a) - (k % len(a)))+q)%len(a)] for q in queries]


k = 123 # just for k 51, both functions return the same result.
a = [39356, 87674, 16667, 54260, 43958, 70429, 53682, 6169, 87496, 
     66190, 90286, 4912, 44792, 65142, 36183, 43856, 77633, 38902, 
     1407, 88185, 80399, 72940, 97555, 23941, 96271, 49288, 27021, 
     32032, 75662, 69161, 33581, 15017, 56835, 66599, 69277, 17144, 
     37027, 39310, 23312, 24523, 5499, 13597, 45786, 66642, 95090, 
     98320, 26849, 72722, 37221, 28255, 60906]
queries = [0,1,47,10,12,13,6,29]

# pa ese caso da igual pero pa otros no! puede ser que funcione
# pa cuando k es menor que len(a)
circularArrayRotation(a, k, queries)==circularArrayRotation2(a, k, queries)

# extralong factorials --------------------------------------------------------
def extraLongFactorials(n):
    if n == 1:
        return 1
    else:
        res = n*extraLongFactorials(n-1)
    return(res)
        
#extraLongFactorials(5)
#   5 * extraLongFactorials(4)
#       4 * extraLongFactorials(3)
#           3 * extraLongFactorials(2)
#               2 * extraLongFactorials(1)
#                       1
#                       = 120
        
        



  
      
       


