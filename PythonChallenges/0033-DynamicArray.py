#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#


def dynamicArray(n, queries):
    # Write your code here
    arr = [[]*n for i in range(n)]
    answers = []
    lastAnswer = 0

    for query in queries:
        idx = ((query[1] ^ lastAnswer) % n)
        if query[0] == 1:
            arr[idx].append(query[2])
        if query[0] == 2:
            lastAnswer = arr[idx][query[2] % len((arr[idx]))]
            answers.append(lastAnswer)
    return answers


if __name__ == '__main__':
    n = 2
    q = 5
    queries = [[1,0,5],[1,1,7],[1,0,3],[2,1,0],[2,1,1]]
    result = dynamicArray(n, queries)
    print(result)