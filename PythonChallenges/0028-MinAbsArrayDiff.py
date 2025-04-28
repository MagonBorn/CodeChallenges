#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def minimumAbsoluteDifference(arr):
    arr.sort()
    minDiff = abs(arr[0] - arr[1])
    for i in range(len(arr)-1):
        if abs(arr[i] - arr[i+1]) < minDiff:
            minDiff = abs(arr[i]-arr[i+1])
    return minDiff


if __name__ == '__main__':
    arr = list(map(int, "3 -7 0".rstrip().split()))
    result = minimumAbsoluteDifference(arr)
    print(result)