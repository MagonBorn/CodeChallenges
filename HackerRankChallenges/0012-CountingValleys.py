#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def countingValleys(steps, path):
    numberOfValleys = 0
    height = 0
    for i in range(steps):
        if path[i] == "U":
            height += 1
        else:
            height -= 1
        if height == -1 and path[i+1] == "U":
            numberOfValleys += 1
    return numberOfValleys


if __name__ == '__main__':
    steps = 8
    path = "UDDDUDUU"
    result = countingValleys(steps, path)
    print(result)
