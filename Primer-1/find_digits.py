#!/bin/python3

import math
import os
import random
import re
import sys

def findDigits(n):
    cnt = 0
    sN = str(n)
    for i in range(len(sN)):
        try:
            if n%int(sN[i])==0:
                cnt += 1
        except: continue
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()

