# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 13:01:26 2019

@author: csmon
"""

# codingame practicing --------------------------------------------------------

# find temperature closes to 0.
# if there is a minus value which its absolute
# value equals a value over 0, the positive numebr should be returned
# if no numbers are given, the result should be "0".

# mine solution
nums = [-5, -4, -2, 12, -40, 4, 2, 18, 11, 5]

# first I sort them from smaller to larger
    # use <= cause want to keep going even if the difference doesnt change
    # cause it could be that an equal positive number is to the right to a 
    # negative numbere and we need to obtain the positive one.
nums.sort()
num = []
diff = float('inf')
for i in nums:

    if (abs(i) <= diff): #and (i < 0):
        num.append(i)
        diff = (abs(i))
num.sort(key = lambda x: -x)
num[0]

# with this one I have the problem that it doesnt return the equal positive
# numebr
diff = float('inf')
target = 0
for i in nums:
    if abs(i - target) < diff:
        final_value = i
        diff = abs(i - target)
final_value

# nice solution using sort and key lambda
# nice explanation of using keys with lambda here:
# https://stackoverflow.com/questions/8966538/syntax-behind-sortedkey-lambda/8966557#8966557

nums = [-5, -4, -2, 12, -40, 4, 2, 18, 11, 5]

# ya cache... primero aplica sort al segundo argumento
# y al resultado de ese aplica sort de nuevo!!
nums.sort(key = lambda x: (abs(x),-x))
print(nums[0])

# showing results
nums = [-5, -4, -2, 12, -40, 4, 2, 18, 11, 5]

# first sorting
# orders from highest to lower
sorted(nums, key = lambda x: (-x)) # a
a = sorted(nums, key = lambda x: (-x))

# second sorting
# orders from smallst to largest but taking into account the absolute 
# value of each item. 
sorted(a, key = lambda x: (abs(x))) # b
b = sorted(a, key = lambda x: (abs(x)))

# return the first element which correspond to the number closer to 
# 0.
print(b[0])



# otros examples --------------------------------------------------------------
(lambda x, y: x / y)(10, 2)


mylist = [(3, 5, 8), (6, 2, 8), ( 2, 9, 4), (6, 8, 5)]
sorted(mylist, key=lambda x: x[1])

mylist.sort(key = lambda x: x[1])
mylist.sort(key = lambda x: x[2])


sorted(mylist, key=lambda x: (x[2],x[1]))

nums.sort()
nums

mylist = [3,6,3,2,4,8,23] 
sorted(mylist)

mylist = [3,6,3,2,4,8,23]
#         0,1,0,1,1,1,0
sorted(mylist, key=lambda x: x%2==0)
#         3,3,23,6,2,4,8