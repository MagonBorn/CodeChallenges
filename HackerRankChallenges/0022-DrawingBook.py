#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#


def pageCount(n, p):
    # Write your code here
    return min(p//2, (n//2)-(p//2))


if __name__ == '__main__':
    n = 6
    p = 2
    result = pageCount(n, p)
    print(result)