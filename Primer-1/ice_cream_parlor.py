#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

def icecreamParlor(m, arr):
    pairs = list(combinations(arr, 2))
    for x,y in pairs:
        if x+y == m:
            if x==y:
                return sorted([arr.index(x)+1, arr.index(y, arr.index(x)+1)+1])
            else:
                return sorted([arr.index(x)+1, arr.index(y)+1])
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

