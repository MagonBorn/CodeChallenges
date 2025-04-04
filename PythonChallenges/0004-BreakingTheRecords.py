#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    min = scores[0]
    max = scores[0]
    records = [0, 0]
    
    for score in scores:
        if score < min:
            records[1] += 1
            min = score
        elif score > max:
            records[0] += 1
            max = score
    print(records)
    return records

if __name__ == '__main__':
    n = 9
    scores = list(map(int, "10 5 20 20 4 5 2 25 1".rstrip().split()))
    result = breakingRecords(scores)