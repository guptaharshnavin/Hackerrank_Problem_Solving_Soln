#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    sticks_cut = []
    while len(arr) != 0:
        min_len = min(arr)
        cnt = 0
        cut_cnt = 0
        while cnt < len(arr):
            arr[cnt] = arr[cnt] - min_len
            cut_cnt += 1
            if arr[cnt] <= 0:
                arr.pop(cnt)
            else:
                cnt += 1
        sticks_cut.append(cut_cnt)
    return sticks_cut

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
