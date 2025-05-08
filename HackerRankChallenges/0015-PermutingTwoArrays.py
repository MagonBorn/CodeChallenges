#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#


def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        if A[i] + B[i] < k:
            return "NO"
    return "YES"


if __name__ == '__main__':
    k = 10
    A = list(map(int, "2 1 3".rstrip().split()))
    B = list(map(int, "7 8 9".rstrip().split()))
    result = twoArrays(k, A, B)
    print(result)

    k = 5
    A = list(map(int, "1 2 2 1".rstrip().split()))
    B = list(map(int, "3 3 3 4".rstrip().split()))
    result = twoArrays(k, A, B)
    print(result)
