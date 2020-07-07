# Sock merchant
# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

from collections import Counter
def sockMerchant(n, ar):
    # first I count the values of each integer
    c=Counter(ar)
    # just get the values of the resulting dictionary, I don't care about the 
    # key
    vals = c.values() 
    # divide by 2 each element
    division = [x/2 for x in vals]
    # get the index of the elements equal or higher than 1
    index =[idx for idx, val in enumerate(division) if val >= 1]
    # get the values of those elements
    vals = [division[i] for i in index]
    # get tne integer value (e.g if value is 1.5 I get one. That would be the results
    # of dividng 3 by 2 for example, we would get only one pair)
    pairs = [int(i) for i in vals]
    # ust sum the resulting integers
    return(sum(pairs))
    

n = 20
ar = [4, 5, 5, 5, 6, 6, 4, 1, 4, 4, 3, 6, 6, 3, 6, 1, 4, 5, 5, 5]

sockMerchant(n, ar)

# this impementation follows the same logic that what is on top but is much 
# mor elegant.
from collections import Counter
def sockMerchant(n, ar):
    sum=0
    for values in Counter(ar).values():
        sum+=values//2
    return sum



sockMerchant(n, ar)

