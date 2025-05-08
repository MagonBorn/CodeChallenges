#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gamingArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def gamingArray(arr):
    cuts = 0
    current = 0

    for val in arr:
        if val > current:
            cuts += 1
            current = val

    return "ANDY" if cuts % 2 == 0 else "BOB"


if __name__ == '__main__':
    arr = list(map(int, "5 2 6 3 4".rstrip().split()))
    result = gamingArray(arr)
    print(result)