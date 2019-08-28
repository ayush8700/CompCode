#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

def maximumPerimeterTriangle(sticks):
    sticks.sort()
    groups = list(combinations(sticks,3))
    triangles = [(x,y,z) for x,y,z in groups if x+y > z and y+z > x and x+z > y]
    if len(triangles) == 0:
        return [-1]
    return max(triangles)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

