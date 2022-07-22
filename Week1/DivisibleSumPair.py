#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    # Write your code here
    rem = [0]*k
    for i in range(len(ar)):
        rem[int(ar[i]%k)] += 1
    count = (rem[0]*(rem[0]-1))/2
    if k%2==0 and k>=2:
        count = count + (rem[int(k/2)]*(rem[int(k/2)]-1))/2
        for i in range(1,int((k/2))):
            count = count + rem[i]*rem[k-i]
    else:
        for i in range(1,int((k+1)/2)):
            count = count + rem[i]*rem[k-i]
    return (int(count))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
