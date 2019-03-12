#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    n = max(p)
    lst = []

    for i in range(1,n+1):
        index = -1
        for (ix,val) in enumerate(p):
            if val == i:
                index = ix + 1
                break
        for (ix,val) in enumerate(p):
            if val == index:
                lst.append(ix + 1)
                break
    return lst

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
