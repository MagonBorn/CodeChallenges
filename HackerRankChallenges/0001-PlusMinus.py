#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    positive = 0
    negative = 0
    zero = 0

    for i in range(len(arr)):
        if arr[i] < 0:
            negative += 1
        elif arr[i] > 0:
            positive += 1
        else:
            zero +=1
    
    print(f'{positive/len(arr):0.6f}')
    print(f'{negative/len(arr):0.6f}')
    print(f'{zero/len(arr):0.6f}')


if __name__ == '__main__':
    # n = int(input().strip())
    n = 6
    # arr = list(map(int, input().rstrip().split()))
    arr = list(map(int, "-4 3 -9 0 4 1".rstrip().split()))

    plusMinus(arr)
