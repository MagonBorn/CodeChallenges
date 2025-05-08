#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#


def missingNumbers(arr, brr):
    return sorted(Counter(brr) - Counter(arr))


if __name__ == '__main__':
    n = 10
    arr = list(map(int, "203 204 205 206 207 208 203 204 205 206".rstrip().split()))
    m = 13
    brr = list(
        map(int, "203 204 204 205 206 207 205 208 203 206 205 206 204".rstrip().split()))
    result = missingNumbers(arr, brr)
    print(result)