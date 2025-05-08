#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def marsExploration(s):
    # Write your code here
    # corruption = 0
    # for i in range(0, len(s), 3):
    #     if s[i] != 'S':
    #         corruption += 1
    #     if s[i + 1] != 'O':
    #         corruption += 1
    #     if s[i + 2] != 'S':
    #         corruption += 1
    # return corruption

    corruption = 0
    for i in range(0, len(s)):
        letter = 'S' if i % 3 == 0 or (i+1) % 3 == 0 else 'O'
        if s[i] != letter:
            corruption += 1
    return corruption


if __name__ == '__main__':
    result = marsExploration("SOSSPSSQSSOR")
    print(result)
