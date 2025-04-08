#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def lonelyinteger(a):
    c = Counter(a)
    # print(c.most_common()[-1][0])
    return c.most_common()[-1][0]


if __name__ == '__main__':
    a = list(map(int, "0 0 1 2 1".rstrip().split()))
    result = lonelyinteger(a)
