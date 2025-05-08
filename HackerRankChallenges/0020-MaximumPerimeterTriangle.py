#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    # Write your code here
    result = -1
    triangle = [-1]
    sticks.sort()
    for i in range(len(sticks) - 2):
        perimeter = sticks[i] + sticks[i+1] + sticks[i+2]
        if sticks[i] + sticks[i+1] > sticks[i+2] and perimeter > result:
            result = perimeter
            triangle = [sticks[i], sticks[i+1], sticks[i+2]]
    return triangle

if __name__ == '__main__':
    sticks = list(map(int, "1 1 1 3 3".rstrip().split()))
    result = maximumPerimeterTriangle(sticks)
    print(" ".join(map(str, result)))