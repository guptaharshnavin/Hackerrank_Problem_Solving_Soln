#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    print(f'A : {a}')
    i = 0
    dist_list = []
    while i < len(a)-1:
        j = i + 1
        dist = len(a)
        while j < len(a):
            if(a[j] == a[i]):
                dist = abs(j-i)
                break
            j += 1
        dist_list.append(dist)
        i += 1
    print(dist_list)
    if(len(dist_list) == 0):
        dist_list.append(-1)
    md = min(dist_list)
    if md == len(a):
        return -1
    else:
        return md

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
