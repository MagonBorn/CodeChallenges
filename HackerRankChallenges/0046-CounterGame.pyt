#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#


def counterGame(n):
    # Count the number of turns in the game
    count = 0
    while n > 1:
        # Determine if n is a power of 2 and divide by 2 if true
        if n > 0 and (n & (n-1)) == 0:
            n = n//2
        else:
            # find the next largest power of 2 from n and subtract it
            n -= (1 << n.bit_length() - 1)
        count += 1
    return "Richard" if count % 2 == 0 else "Louise"


if __name__ == '__main__':
  n = int("132".strip())
  result = counterGame(n)
  print(result)