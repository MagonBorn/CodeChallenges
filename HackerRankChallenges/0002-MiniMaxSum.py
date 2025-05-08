#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    sum1=0
    sum2=0
    for i in range(0,4):
        sum1 += arr[i]
    for i in range(len(arr) -1, 0, -1):
        sum2 += arr[i]
    print(sum1, sum2)

if __name__ == '__main__':

    # arr = list(map(int, input().rstrip().split()))
    arr = list(map(int, "1 2 3 4 5".rstrip().split()))

    miniMaxSum(arr)
