#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    print(4294967295-n)
    return 4294967295-n

if __name__ == '__main__':
  result = flippingBits(2147483647)
