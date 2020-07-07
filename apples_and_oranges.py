import math
import os
import random
import re
import sys


# https://www.hackerrank.com/challenges/apple-and-orange/problem

# I need to give the input manually for input. ....

st = input().split()

s = int(st[0])

t = int(st[1])

ab = input().split()

a = int(ab[0])

b = int(ab[1])

mn = input().split()

m = int(mn[0])

n = int(mn[1])

apples = list(map(int, input().rstrip().split()))

oranges = list(map(int, input().rstrip().split()))

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    print(sum([(x + a) >= s and (x + a) <= t for x in apples]))
    print(sum([(x + b) >= s and (x + b) <= t for x in oranges]))

