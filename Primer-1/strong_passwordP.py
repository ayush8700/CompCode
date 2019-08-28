#!/bin/python3

import math
import os
import random
import re
import sys

def minimumNumber(n, password):
    if len(password) < 6:
        return 6 - len(password)
    
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    cnt = {}
    for ch in password:
        if ch in numbers:
            cnt['num'] = 1
        elif ch in lower_case:
            cnt['lc'] = 1
        elif ch in upper_case:
            cnt['uc'] = 1
        elif ch in special_characters:
            cnt['sc'] = 1
    lenk = len(cnt.keys())
    if lenk <= 4 and len(password) >= 6:
        return 4 - lenk
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()

