#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    a.sort()
    
    arrLength = 0
    start = 0
    
    for i in range(len(a)):
        if a[i] - a[start] <= 1:
            if i - start >= arrLength:
                arrLength+=1
        else:
            start = i
    return arrLength
    


if __name__ == '__main__':
    a = list(map(int, "4 6 5 3 3 1".rstrip().split()))
    result = pickingNumbers(a)
    print(result)
