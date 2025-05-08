#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    time = s.split(":")
    
    if time[2][2:] == "PM" and time[0] < "12":
        time[0] = int(time[0]) + 12
    elif time[2][2:] == "AM" and time[0] == "12":
        time[0] = "00"
    time[2] = time[2][:2]

    return ":".join(str(element) for element in time)
    
if __name__ == '__main__':
    s = "07:05:45PM"
    result = timeConversion(s)
    print(result)