#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumPasses' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER m
#  2. LONG_INTEGER w
#  3. LONG_INTEGER p
#  4. LONG_INTEGER n
#

def minimumPasses(m, w, p, n):
    # Write your code here
    def canReach(target_passes):
        machines = m
        workers = w
        candies = 0
        passes = 0

        while passes < target_passes:
            max_possible = candies + machines * workers * (target_passes - passes)
            if max_possible >= n:
                return True

            if candies < p:
                needed = p - candies
                extra_passes = math.ceil(needed / (machines * workers))
                passes += extra_passes
                candies += extra_passes * machines * workers
                if passes >= target_passes:
                    return False

            buy = candies // p
            total = machines + workers + buy
            half = total // 2

            if machines > workers:
                machines = max(machines, half)
                workers = total - machines
            else:
                workers = max(workers, half)
                machines = total - workers

            candies -= buy * p
            candies += machines * workers
            passes += 1

        return candies >= n

    low = 1
    high = 10**18
    answer = high

    while low <= high:
        mid = (low + high) // 2
        if canReach(mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    w = int(first_multiple_input[1])

    p = int(first_multiple_input[2])

    n = int(first_multiple_input[3])

    result = minimumPasses(m, w, p, n)

    fptr.write(str(result) + '\n')

    fptr.close()
