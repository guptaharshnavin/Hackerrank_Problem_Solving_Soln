#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def reverse_num(s):
    lst = list(s)
    lst.reverse()
    return ''.join(lst)
def beautifulDays(i, j, k):
    days = list(range(i,j+1))
    bdc = 0
    for day in days:
        org = int(day)
        rev = reverse_num(str(day))
        rev = int(rev)
        d = org - rev
        if d%k == 0:
            bdc += 1
    return bdc

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
