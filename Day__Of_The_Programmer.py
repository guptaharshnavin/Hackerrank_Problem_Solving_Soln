#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    leapYear = False
    if year <= 1917:
        if year % 4 == 0:
            day = '12.09.' + str(year)
            print(day)
        else:
            day = '13.09.' + str(year)
            print(day)
    elif year >= 1919:
        if year % 400 == 0:
            day = '12.09.' + str(year)
        elif year % 4 == 0 and year % 100 != 0:
            day = '12.09.' + str(year)
        else:
            day = '13.09.' + str(year)
    else:
        day = '26.09.' + str(year)
    return day


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
