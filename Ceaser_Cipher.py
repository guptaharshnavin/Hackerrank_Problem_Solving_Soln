#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    coded = ""

    for c in s:
        if c.isalpha():
            val = ord(c)
            val = val + k
            if c.isupper():
                while val > 90:
                    val = val - (90 + 1)
                    val = ord('A') + val
            else:
                while val > 122:
                    val = val - (122 + 1)
                    val = ord('a') + val
            coded = coded + chr(val)
        else:
            coded = coded + c
    return(coded)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
