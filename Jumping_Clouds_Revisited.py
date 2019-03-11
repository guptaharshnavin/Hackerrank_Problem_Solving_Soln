#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    print(c)
    print(k)

    energy = 100
    index_cnt = 0

    while True:
        tmp = index_cnt + k
        if(tmp >= len(c)):
            if c[0] == 1:
                energy -=3
            else:
                energy -= 1
            break
        else :
            if c[tmp] == 1:
                energy -= 2
            energy -= 1
            index_cnt = tmp
    return energy
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
