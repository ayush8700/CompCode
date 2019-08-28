#!/bin/python3

import math
import os
import random
import re
import sys

def luckBalance(k, contests):
    li = []
    maxLuck = 0
    for x,y in contests:
        if y == 1:
            li.append([x,y])
        else:
            maxLuck += x
    li.sort(reverse=True)
    for x,y in li[:k]:
        maxLuck += x
    for x,y in li[k:]:
        maxLuck -= x
    return maxLuck
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()

