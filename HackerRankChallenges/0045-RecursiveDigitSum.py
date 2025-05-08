#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#


def superDigit(n, k):
    # Write your code here
    # if len(n) == 1:
    #     return int(n)

    # total = 0
    # for number in n:
    #     total += int(number)

    # total = total * k

    # return superDigit(str(total), 1)

    return superDigit(sum(int(i) for i in str(n)) * k, 1) if len(str(n)) != 1 else n


if __name__ == '__main__':
    n = "9875"
    k = 4
    result = superDigit(n, k)
    print(result)