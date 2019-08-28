#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

def maximizingXor(l, r):
    li = [i for i in range(l,r+1)]
    pairs = list(combinations(li,2))
    return max([x ^ y for x,y in pairs])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input())

    r = int(input())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()

