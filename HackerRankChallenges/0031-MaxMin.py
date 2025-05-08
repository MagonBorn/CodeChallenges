#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#


def maxMin(k, arr):
    # Write your code here
    arr.sort()
    diff = arr[k - 1] - arr[0]
    for i in range(len(arr) - k + 1):
        currDiff = arr[k+i-1] - arr[i]
        if currDiff < diff:
            diff = currDiff
    return diff


if __name__ == '__main__':
    n = 7
    k = 3
    arr = [10, 100, 300, 200, 1000, 20, 30]
    result = maxMin(k, arr)
    print(result)