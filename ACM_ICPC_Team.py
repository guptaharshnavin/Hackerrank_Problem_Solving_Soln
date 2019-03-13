#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
    attendees = len(topic)
    subjects = len(topic[0])
    topics_known = []
    i = 0

    while i < (attendees-1):
        p1 = topic[i]
        j = i + 1
        while j < attendees:
            p2 = topic[j]
            index = 0
            count = 0
            while index < subjects:
                if p1[index] == '1' or p2[index] == '1':
                    count += 1
                index += 1
            topics_known.append(count)
            j += 1
        i += 1
    r = []
    m = max(topics_known)
    r.append(m)
    count = 0
    for topic in topics_known:
        if topic == m:
            count += 1
    r.append(count)
    return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
