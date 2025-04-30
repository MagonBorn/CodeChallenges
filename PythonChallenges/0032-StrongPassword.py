#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#


def minimumNumber(n, password):
    conditions = 0
    specialCharacters = re.compile("[!@#$%^&*()\\-+]")
    if not bool(re.search("[a-z]", password)):
        conditions += 1
    if not bool(re.search("[A-Z]", password)):
        conditions += 1
    if not bool(re.search("[0-9]", password)):
        conditions += 1
    if not bool(re.search(specialCharacters, password)):
        conditions += 1
    if conditions + len(password) < 6:
        conditions += 6 - (conditions + len(password))
    return conditions


if __name__ == '__main__':
    n = 11
    password = "#HackerRank"
    answer = minimumNumber(n, password)
    print(answer)