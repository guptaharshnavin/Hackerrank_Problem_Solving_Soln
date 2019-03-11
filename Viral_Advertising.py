#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    print(n)
    liked = math.floor(5/2)
    cumulative = liked

    for i in range(n-1):
        t = liked * 3
        print(f'T : {t}')
        liked = math.floor(t/2)
        print(f'Liked : {liked}')
        cumulative += liked
        print(f'Cumulative : {cumulative}')
    return cumulative

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
