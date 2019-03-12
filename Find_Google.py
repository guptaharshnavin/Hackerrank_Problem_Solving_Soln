#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    string = input()
    g_list = ['g','G']
    o_list = ['o','O','0']
    open_bracket_list = ['(','[','<']
    close_bracket_list = [')',']','>']
    l_list = ['l','L','I']
    e_list = ['e','E','3']

    index = 0
    word = []
    while index < len(string):
        c = string[index]
        if c in open_bracket_list:
            t = string[index+1]
            if t in  close_bracket_list:
                word.append('O')
                index += 2
        else:
            word.append(c)
            index += 1
    correct = True
    if len(word) != 6:
        correct = False
    else:
        if word[0] not in g_list:
            correct = False
        if word[1] not in o_list:
            correct = False
        if word[2] not in o_list:
            correct = False
        if word[3] not in g_list:
            correct = False
        if word[4] not in l_list:
            correct = False
        if word[5] not in e_list:
            correct = False

    if correct == True:
        print("True")
    else:
        print("False")
