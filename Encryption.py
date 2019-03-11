#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    print(s)
    length = len(s)
    rows = math.floor(math.sqrt(length))
    columns = math.ceil(math.sqrt(length))
    #print(f'Rows : {rows}')
    #print(f'Columns : {columns}')

    while True:
        if (rows*columns) < length:
            rows += 1
        else:
            break
    matrix = [['$' for i in range(columns)]for j in range(rows)]
    counter = 0
    for i in range(rows):
        for j in range(columns):
            if counter == length:
                break
            else:
                matrix[i][j] = s[counter]
                counter += 1
    #for row in matrix:
    #    print(row)
    final_message = ""
    for j in range(columns):
        for i in range(rows):
            c = matrix[i][j]
            if c == '$':
                break
            else:
                final_message = final_message + c
        final_message = final_message + ' '
    #print(final_message)
    return final_message

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
