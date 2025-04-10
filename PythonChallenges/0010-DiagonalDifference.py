#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    # Write your code here
    lefToRightDiagonal = 0
    rightToLeftDiagional = 0
    leftPointer = 0
    rightPointer = len(arr) - 1
    for i in range(len(arr)):
        lefToRightDiagonal += arr[i][leftPointer]
        rightToLeftDiagional += arr[i][rightPointer]
        leftPointer += 1
        rightPointer -= 1

    return abs(lefToRightDiagonal - rightToLeftDiagional)


if __name__ == '__main__':
    arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    result = diagonalDifference(arr)
    print(result)