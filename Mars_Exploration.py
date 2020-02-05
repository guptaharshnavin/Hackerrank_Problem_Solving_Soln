#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    print(s)

    org_string = "SOS" * int((len(s)/3))
    print(org_string)
    
    diff_count = 0
    i = 0

    while i < len(s):
        if s[i] != org_string[i]:
            diff_count = diff_count + 1
        i = i + 1
    
    return(diff_count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
