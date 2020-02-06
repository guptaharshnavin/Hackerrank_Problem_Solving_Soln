#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    word_dict = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"quarter",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",21:"twenty one",22:"twenty two",23:"twenty three",24:"twenty four",25:"twenty five",26:"twenty six",27:"twenty seven",28:"twenty eight",29:"twenty nine",30:"half"}

    output = ""

    if m == 0:
        output = word_dict[h] + " o' clock"
    elif m <= 30:
        if m == 15 or m == 30:
            output = word_dict[m]
        elif m == 1:
            output = word_dict[m] + " minute"
        else:
            output = word_dict[m] + " minutes"
        output = output + " past " + word_dict[h]
    else:
        mint = 60 - m
        if mint == 15:
            output = word_dict[mint]
        elif mint == 1:
            output = word_dict[mint] + " minute"
        else:
            output = word_dict[mint] + " minutes"
        
        hr = h + 1
        if hr > 12:
            hr = hr - 12
        output = output + " to " + word_dict[hr]
    return(output)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
