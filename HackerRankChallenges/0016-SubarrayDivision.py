#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):       
    length = 0
    currentTotal = 0
    numOfSegments = 0
    left = 0
    
    for i in range(len(s)):
        currentTotal+= s[i]
        length+=1
        if length >= m:
            if currentTotal== d:
                numOfSegments+=1
            currentTotal-=s[left]
            left+=1
            length-=1
        
    return numOfSegments
            
        
if __name__ == '__main__':
    s = list(map(int, "2 2 1 3 2".rstrip().split()))
    d = 4
    m = 2
    result = birthday(s, d, m)
    print(result)
