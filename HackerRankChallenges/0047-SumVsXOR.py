#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#


def sumXor(n):
    # return n to the power:
    # numbers of bits in the binary n subtracted by the number of 1's in the binary n
    # We count the number of 0's in the bit essentially
    return 2 ** (n.bit_length() - n.bit_count())


if __name__ == '__main__':
  n = int("10".strip())
  result = sumXor(n)
  print(result)