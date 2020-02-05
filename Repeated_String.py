#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    str_len = len(s)
    mul_floor = math.floor(n / str_len)
    org_count = (s.count("a")) * mul_floor
    
    rem_len = n - (str_len * mul_floor)

    if rem_len != 0:
        new_str = s[:rem_len]
        org_count = org_count + new_str.count("a")

    return(org_count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
