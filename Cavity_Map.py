#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    new_grid = grid.copy()

    rows = len(grid)
    columns = len(grid[0])

    for r in range(rows):
        new_grid[r] = list(grid[r])
        grid[r] = list(grid[r])
    
    print(new_grid)

    for r in range(rows):
        if r == 0 or r == (rows - 1):
            continue

        for c in range(columns):
            if c == 0 or c == (columns - 1):
                continue
            
            curr_row = r
            curr_col = c
            curr_v = int(grid[curr_row][curr_col])

            n_left = int(grid[curr_row][curr_col - 1])
            n_right = int(grid[curr_row][curr_col + 1])
            n_up = int(grid[curr_row - 1][curr_col])
            n_down = int(grid[curr_row + 1][curr_col])

            if (curr_v > n_left) and (curr_v > n_right) and (curr_v > n_up) and (curr_v > n_down):
                new_grid[curr_row][curr_col] = "X"
        
    grid_n = []
    for r in range(rows):
        temp = ""
        for c in range(columns):
            temp = temp + new_grid[r][c]
        grid_n.append(temp)
    print(grid_n)
    return(grid_n)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
