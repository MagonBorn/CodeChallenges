#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#


def sockMerchant(n, ar):
    # Write your code here
    ar.sort()
    count = 0
    current = 1

    for i in range(n - 1):
        if ar[i] == ar[i+1]:
            current += 1
        else:
            count += current//2
            current = 1
    count += current//2
    return count


if __name__ == '__main__':
    n = 9
    ar = list(map(int, "10 20 20 10 10 30 50 10 20".rstrip().split()))
    result = sockMerchant(n, ar)
    print(result)
