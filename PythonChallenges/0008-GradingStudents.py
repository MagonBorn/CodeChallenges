#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def gradingStudents(grades):
    result = [grade + 5 - grade % 5 if grade > 37 and ((grade % 5) > 2) else grade for grade in grades]
    print(result)
    return result


if __name__ == '__main__':
    grades = [73, 67, 38, 33]
    result = gradingStudents(grades)