#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getFinalData' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY data
#  2. 2D_INTEGER_ARRAY updates
#

def getFinalData(data, updates):
    n = len(data)
    
    flip = [0] * (n + 1)# extra array to track flips
    
    for l, r in updates:#mark where flips start and end
        flip[l-1] += 1
        if r < n:
            flip[r] -= 1
    
    curr = 0
    for i in range(n):#apply prefix sum and flip if odd
        curr += flip[i]
        if curr % 2 == 1:  # odd -> flip sign
            data[i] = -data[i]
    
    return data



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    data_count = int(input().strip())

    data = []

    for _ in range(data_count):
        data_item = int(input().strip())
        data.append(data_item)

    updates_rows = int(input().strip())
    updates_columns = int(input().strip())

    updates = []

    for _ in range(updates_rows):
        updates.append(list(map(int, input().rstrip().split())))

    result = getFinalData(data, updates)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
