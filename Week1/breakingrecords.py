#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    countmax = -1
    countmin = -1
    maximum = float('-inf')
    minimum = float('inf')
    for i in range(len(scores)):
        if scores[i] > maximum:
            countmax +=1
            maximum = max(maximum,scores[i])
        if scores[i] < minimum:
            countmin += 1
            minimum = min(minimum, scores[i])
    return [countmax,countmin]
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
