#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    print(type(n))
    print(n)

    height = 1
    counter = 0
    spring = True

    while counter <= n:
        if counter == 0:
            height = height
        else:
            if counter % 2 == 0:
                #Summer Season
                height += 1
            else:
                height = height * 2
        counter += 1
    return height


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
