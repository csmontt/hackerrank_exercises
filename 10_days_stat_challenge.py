# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 21:42:04 2019

@author: csmon
"""

import numpy as np
from scipy import stats

size = int(input())
numbers = list(map(int, input().split()))
print(np.mean(numbers))
print(np.median(numbers))
print(int(stats.mode(numbers)[0]))