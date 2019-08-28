#!/bin/python3

import math
import os
import random
import re
import sys

def pangrams(s):
    dy = {}
    for ch in s:
        if ch in dy.keys():
            dy[ch] += 1
        else:
            dy[ch] = 1
    if len(dy.keys()) >= 27:
        return 'pangram'
    else:
        return 'not pangram'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()

