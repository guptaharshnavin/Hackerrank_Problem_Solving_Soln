#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    square_count = 0
    base = math.floor(math.sqrt(a))
    print(f'Base : {base}')
    sq = base ** 2
    print(f'Square : {sq}')

    while sq <= b:
        if sq < a:
            square_count = square_count
            base += 1
            sq = base ** 2
        else:
            square_count += 1
            base += 1
            sq = base ** 2
    return square_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
