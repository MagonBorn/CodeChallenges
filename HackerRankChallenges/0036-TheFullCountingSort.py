#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#


def countSort(arr):
    # Find the mid point of the list and create an empty array equal to half the length + 1
    mid = int(len(arr)/2)
    result = [[]*mid for i in range(mid + 1)]

    # Loop through each int/string pair
    for i in range(len(arr)):
        # store the current pairs int
        idx = int(arr[i][0])
        # If associated int is in the first half of the array, append a dash to the result array at index
        # of the associated int, else add the associated string
        if i < mid:
            result[idx].append(chr(45))
        else:
            result[idx].append(arr[i][1])

    # Flatten the list and join all elements into a string
    res = ([el for sub in result for el in sub])
    print(" ".join(res))


if __name__ == '__main__':
    n = 20

    arr = [[0, "ab"], [6, "cd"], [0, "ef"], [6, "gh"], [4, "ij"], [0, "ab"], [6, "cd"], [0, "ef"], [6, "gh"], [0, "ij"], [4, "that"], [3, "be"], [0, "to"], [1, "be"], [5, "question"], [1, "or"], [2, "not"], [4, "is"], [2, "to"], [4, "the"]]
    countSort(arr)
