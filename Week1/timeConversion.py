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
    # Write your code here
    
    hh = int(s[0:2])
    ti = s[8]
    if ti == 'A' and hh == 12:
        c = '00'
        return(c + s[2:8])
    elif ti == 'A' and hh < 12:
        return(s[:8])
    elif ti == 'P' and hh < 12:
        c = hh+12
        return(str(c) + s[2:8])
    else:
        return(s[:8])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
