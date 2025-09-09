#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getPotentialOfWinner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY potential
#  2. LONG_INTEGER k
#

def getPotentialOfWinner(potential, k):
    # Write your code here
    n = len(potential)
    
    if k >= n:
        return max(potential)
    
    current_winner = potential[0]
    consecutive_wins = 0
    i = 1
    
    while True:
        challenger = potential[i]
        
        if current_winner > challenger:
            consecutive_wins += 1
        else:
            current_winner = challenger
            consecutive_wins = 1
        i += 1
        
        if consecutive_wins == k:
            return current_winner
            
        if i == n:
            i = 1
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    potential_count = int(input().strip())

    potential = []

    for _ in range(potential_count):
        potential_item = int(input().strip())
        potential.append(potential_item)

    k = int(input().strip())

    result = getPotentialOfWinner(potential, k)

    fptr.write(str(result) + '\n')

    fptr.close()
