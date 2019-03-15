#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    wrappers = n/c
    chocolate_count = wrappers

    while wrappers >= m:
        temp = int(wrappers/m)
        print("----------------------")
        print(f'Temp : {temp}')
        chocolate_count += temp
        wrappers = wrappers - (m*temp)
        print(f'Wrapper : {wrappers}')
        wrappers = wrappers + temp
        print(f'Wrappers : {wrappers}')
    return int(chocolate_count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
