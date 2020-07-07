# counting valleys

# https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup


import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    height = 0
    valleys = 0
    for i in s: #use list compression!
        if i == "D":
            height += -1
        else:
            height += 1
        if (height == 0 and i == "U"):
            valleys += 1
    return(valleys)
    
steps = ["U","D", "D", "D", "U","D","U","U","U","D"]

countingValleys(n, steps)


    
    

