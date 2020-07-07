# Hash tables: ransom note
# I assume I need to use a hash table but im using sets here
# doesnt work cause intersection doesnt considered elements that appear more
# than one time
# e.g. doest work for 

# magazine = two times three is not four
# note = two times two is four

import math
import os
import random
import re
import sys

magazine = ['give', 'me', 'one', 'grand', 'today', 'night']
note = ['give', 'one', 'grand', 'today', 'night']

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine = set(magazine)
    note = set(note)
    if (len(note.intersection(magazine))==len(note)):
        print('Yes')
    else:
        print('No')
        
checkMagazine(magazine, note)

hash(magazine[0])