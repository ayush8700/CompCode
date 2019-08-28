#!/bin/python3

import math
import os
import random
import re
import sys

def closestNumbers(arr):
    arr.sort()
    li = []
    for i in range(len(arr)-1):
        li.append((arr[i], arr[i+1]))
    diffList = [abs(x-y) for x,y in li]
    mn = min(diffList)
    li2 = []
    for x,y in li:
        if abs(x-y) == mn:
            li2.append(x)
            li2.append(y)
    return li2
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

