#!/bin/python3

import math
import os
import random
import re
import sys

def marcsCakewalk(calorie):
    minDist = 0
    calorie.sort(reverse=True)
    for i in range(len(calorie)):
        minDist += (2**i) * calorie[i]
    return minDist

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()

