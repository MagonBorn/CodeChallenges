#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    return 2 if m==1 or n % 2 ==0 else 1
    

if __name__ == '__main__':
    print(towerBreakers(1, 7))
    print(towerBreakers(2, 3))
    print(towerBreakers(1, 4))
    print(towerBreakers(3, 7))
    print(towerBreakers(2, 2))
