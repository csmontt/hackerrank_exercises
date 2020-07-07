# Jumping on the clouds

#https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen

import math
import os
import random
import re
import sys

n = 6
c = [0,0,0,1,0]

# the last its always zero? yes
# it always start with 0 too

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    steps = 0
    index = 0
    for i in range(len(c)):
        if (index == len(c)-1):
            break
        elif (index < len(c)-2 and c[index+2] != 1):
            index += 2
            steps += 1
        else:
            index += 1
            steps += 1
    return(steps)
    

jumpingOnClouds(c)
    
    
