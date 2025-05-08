#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    if x1 == x2:
        return "YES"
    if v1 == v2:
        return "NO"

    relative_speed = v2 - v1
    initial_distance = x1 - x2
    jumps = initial_distance / relative_speed

    if jumps == abs(int(jumps)):
        return "YES"

    return "NO"

if __name__ == '__main__':
    x1 = 0
    v1 = 3
    x2 = 4
    v2 = 2
    result = kangaroo(x1, v1, x2, v2)
    print(result)