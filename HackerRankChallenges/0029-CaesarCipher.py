#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def caesarCipher(s, k):
    # Write your code here
    result = ""
    for i in range(len(s)):
        char = s[i]
        if char.isupper():
            result += chr((ord(char) + k-65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + k-97) % 26 + 97)
        else:
            result += char
    return result


if __name__ == '__main__':
    s = "Hello_World!"
    k = 4
    result = caesarCipher(s, k)
print(result)