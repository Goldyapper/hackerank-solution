#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the riddle function below.
def riddle(arr):
    n = len(arr)
    res = [0] * (n + 1)
    stack = []
    left = [-1] * n
    right = [n] * n

    # Find the index of the previous smaller element for each element
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)

    stack.clear()

    # Find the index of the next smaller element for each element
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)

    # Compute the length of the window where arr[i] is the minimum
    for i in range(n):
        length = right[i] - left[i] - 1
        res[length] = max(res[length], arr[i])

    # Fill in the rest of the result array
    for i in range(n - 1, 0, -1):
        res[i] = max(res[i], res[i + 1])

    return res[1:]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = riddle(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
