#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the serviceLane function below.
def serviceLane(n, cases,width):
    ans = []

    for c in cases:
        temp_list = width[c[0]:c[1] + 1]
        min_w = min(temp_list)
        ans.append(min_w)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nt = input().split()

    n = int(nt[0])

    t = int(nt[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(n, cases,width)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
