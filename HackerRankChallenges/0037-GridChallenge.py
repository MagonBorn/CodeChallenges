#!/bin/python3

import math
import os
import random
import re
import sys
import timeit

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # print(f'Matrix 1: {timeit.timeit(lambda: [sorted(list(row)) for row in grid], number=10000000)}')
    # print(
    #     f'Matrix 2: {timeit.timeit(lambda: [sorted(list(el)) for el in grid], number=10000000)}')
    # print(
    #     f'Matrix 3: {timeit.timeit(lambda: [sorted(map(str, el)) for el in grid], number=10000000)}')
    # print(
    #     f'Matrix 4: {timeit.timeit(lambda: [sorted(i) for y, i in enumerate(grid)], number=10000000)}')
    
    # Timing Results
    # Matrix 1: 16.272592199995415
    # Matrix 2: 17.04190319999907
    # Matrix 3: 28.777980200000457
    # Matrix 4: 14.84266440000647
    
    matrix = [sorted(i) for y, i in enumerate(grid)]
    for i in range(len(grid)-1):
      for j in range(len(grid[0])):
        if ord(grid[i][j]) > ord(grid[i+1][j]):
          return "NO"
    return "YES"
    
if __name__ == '__main__':
   grid = ["eabcd", "fghij", "olkmn", "trpqs", "xywuv"]
   result = gridChallenge(grid)
   print(result)