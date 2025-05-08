#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    birds = Counter(arr).most_common()
    birdID = birds[0][0]
    birdFrequency = birds[0][1]
    
    for bird in birds:
        if birdFrequency == bird[1] and bird[0] < birdID:
            birdID = bird[0]
            birdFrequency = bird[1]
    return birdID
    
    

if __name__ == '__main__':
  arr = list(map(int, "1 4 4 4 5 3".rstrip().split()))
  result = migratoryBirds(arr)
  print(result)