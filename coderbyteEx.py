# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 10:22:30 2019

@author: csmon
"""

# factorial -------------------------------------------------------------------
def FirstFactorial(num): 
    ind = num
    while ind > 1:
        num = num * (ind-1)
        ind = ind - 1
    return num
    
# keep this function call here  
FirstFactorial(4)  


def extraLongFactorials(n):
    if n == 1:
        return 1
    else:
        res = n*extraLongFactorials(n-1)
    return(res)
    
extraLongFactorials(4)


# reverse string --------------------------------------------------------------
s = "Hola a todos"

def FirstReverse(str): 
    new_string = []
    for i in range(len(str)):
        new_string.append(str[len(str)-(i+1)])
    return(''.join(new_string))


def FirstReverse(str): 
    return str[::-1]

FirstReverse("Valeria")
