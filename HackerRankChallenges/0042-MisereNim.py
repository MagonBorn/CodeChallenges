#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

#
# Complete the 'misereNim' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY s as parameter.
#


def misereNim(s):
    # Write your code here
    xor = reduce((lambda x, y: x ^ y), s)
    if max(s) == 1:
        return "First" if xor == 0 else "Second"
    else:
        return "Second" if xor == 0 else "First"


if __name__ == '__main__':
    s = list(map(int, "9 8 4 4 4 7".rstrip().split()))
    result = misereNim(s)
    print(result)