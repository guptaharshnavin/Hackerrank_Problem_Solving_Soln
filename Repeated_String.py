#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    print(f'S : {s}')
    print(f'N : {n}')
    search_count = 0
    total_count = 0

    for c in s:
        if c == 'a' or c == 'A':
            search_count += 1
    print(f'Search Count : {search_count}')
    length = len(s)
    m_len = int(n/length)
    a_len = (length * m_len) + 1
    total_count = search_count * m_len
    
    index = 0
    while a_len <= n:
        if index == length:
            index = 0
        if s[index] == 'A' or s[index] == 'a':
            total_count += 1
        a_len += 1
        index += 1
    return int(total_count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
