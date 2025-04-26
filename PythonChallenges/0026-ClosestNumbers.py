#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    arr.sort()
    minDiff = arr[1] - arr[0]
    result = []
    
    for i in range(len(arr)-1):
        currDiff = arr[i+1] - arr[i]
        if currDiff < minDiff:
            minDiff = currDiff
    
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] == minDiff:
            result.extend([arr[i], arr[i+1]])
    
    return result
    
if __name__ == '__main__':
    arr = list(map(int, "-20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854".rstrip().split()))
    result = closestNumbers(arr)
    print(result)