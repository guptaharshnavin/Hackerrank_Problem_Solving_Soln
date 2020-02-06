#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    sums = 2015

    s = s.upper()
    s_set = set(s)

    sumi = 0
    for c in s_set:
        if c.isalpha():
            sumi = sumi + ord(c)

    if sumi == sums:
        return("pangram")
    else:
        return("not pangram")
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
