#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    print(f'P : {p}')
    print(f'D : {d}')
    print(f'M : {m}')
    print(f'S : {s}')

    total_spent = 0
    games_count = 0
    print("-------------------")
    while (p >= m) and (total_spent <= s) and(p <= s):
        print(f'P : {p}')
        print(f'Total Spent : {total_spent}')
        print(f'Games Count : {games_count}')
        total_spent += p
        if(total_spent <= s):
            games_count += 1
        p = p - d

    while True:
        print(f'P : {p}')
        print(f'Total Spent : {total_spent}')
        print(f'Games Count : {games_count}')
        if(total_spent + m <= s) and (p <= s):
            total_spent += m
            games_count += 1
        else:
            break
    print(f'P : {p}')
    print(f'Total Spent : {total_spent}')
    print(f'Games Count : {games_count}')
    return games_count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
