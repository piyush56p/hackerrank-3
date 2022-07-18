#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    minimum = float('inf')
    maximum = float('-inf')
    arr.sort()
    
    maximum = sum(arr[0:4])
    
    minimum = sum(arr[1:5])
    print(maximum, minimum)
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
