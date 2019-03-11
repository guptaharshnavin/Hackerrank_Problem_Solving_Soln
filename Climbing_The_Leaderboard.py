#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    sorted(scores,reverse = True)
    #print(f'Scores : {scores}')
    #print(f"Alice's Scores : {alice}")
    alice_ranks = []
    rank_count = 0

    for a_scr in alice:
        #a_scr : Score Of Alice In Particular Games
        index_value = -1
        if a_scr in scores:
            index_value = scores.index(a_scr)
        else:
            index_value = len(scores) - 1
        #print(index_value)

        counter = 0
        prev_scr = 0
        rank_count = 0
        got_rank = False
        prev_scr = 0

        while counter <= index_value:
            scr = scores[counter]
            #print(scr)
            counter += 1
            if a_scr >= scr:
                alice_ranks.append(rank_count+1)
                got_rank = True
                break
            elif prev_scr == scr:
                prev_scr = scr
            else:
                rank_count += 1
                prev_scr = scr
        if got_rank == False:
            alice_ranks.append(rank_count+1)
    #print(alice_ranks)
    return alice_ranks

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
