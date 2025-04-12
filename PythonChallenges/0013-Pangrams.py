#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def pangrams(s):
    sentance = s.lower()
    alphabet = [chr(i) for i in range(ord("a"), ord("z"))]
    for i in alphabet:
        if i.lower() not in sentance:
            return 'not pangram'
    return 'pangram'


if __name__ == '__main__':
    s = "We promptly judged antique ivory buckles for the next prize"
    result = pangrams(s)
    print(result)

