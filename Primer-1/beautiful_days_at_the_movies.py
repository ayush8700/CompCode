#!/bin/python3

import math
import os
import random
import re
import sys

def beautifulDays(i, j, k):
    cnt = 0
    for num in range(i,j+1):
        rev = int(str(num)[::-1])
        if (num - rev)%k == 0:
            cnt += 1
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()

