#!/bin/python3

import math
import os
import random
import re
import sys

def utopianTree(n):
    if n == 0:
        return 1

    height = 1
    for i in range(1, n+1):
        if i%2==0:
            height += 1
        else:
            height = 2*height
    return height

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()

