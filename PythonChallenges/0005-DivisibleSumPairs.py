#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    result = 0
    for i in range(0, len(ar)):
        for j in range(i+1, len(ar)):
            if i < j and ((ar[i] + ar[j]) % k == 0):
                result += 1
    print(result)
    return result

if __name__ == '__main__':

    first_multiple_input = "1 3 2 6 1 2".rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    ar = list(map(int, "1 3 2 6 1 2".rstrip().split()))
    result = divisibleSumPairs(n, k, ar)
