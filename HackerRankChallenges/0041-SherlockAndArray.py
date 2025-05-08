#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def balancedSums(arr):
    # Write your code here
    total_sum = 0
    for value in arr:
        total_sum += value

    left_sum = 0
    for value in arr:
        right_sum = total_sum - left_sum - value
        if left_sum == right_sum:
            return "YES"
        left_sum += value

    return "NO"


if __name__ == '__main__':
  arr = list(map(int, "1 2 3 3".rstrip().split()))
  result = balancedSums(arr)
  print(result)
