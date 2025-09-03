#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'reverseShuffleMerge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def reverseShuffleMerge(s):
    total = Counter(s)
    required = {c: total[c] // 2 for c in total}
    used = Counter()
    remain = Counter(s)
    result = []

    for c in reversed(s):
        remain[c] -= 1

        # Skip if we already used enough of this char
        if used[c] >= required[c]:
            continue

        # Maintain lexicographical order
        while result:
            last = result[-1]
            # Can we pop the last character?
            if (c < last and
                used[last] + remain[last] > required[last]):
                used[last] -= 1
                result.pop()
            else:
                break

        result.append(c)
        used[c] += 1

    return ''.join(result)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()
