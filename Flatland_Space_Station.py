#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    print(f'N : {n}')
    print(f'C : {c}')

    c.sort()
    city_list = list(range(0,n))
    print(city_list)
    distance_list = []

    index = 0
    for city in city_list:
        temp_list = []
        for sp in c:
            res = abs(city - sp)
            temp_list.append(res)
        min_d = min(temp_list)
        distance_list.append(min_d)
    return max(distance_list)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
