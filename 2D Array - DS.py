#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    max_sum = -63  # Minimum possible hourglass sum (-9 * 7)
    for i in range(4):
        for j in range(4):
            top = sum(arr[i][j:j+3])
            middle = arr[i+1][j+1]
            bottom = sum(arr[i+2][j:j+3])
            current_sum = top + middle + bottom
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
