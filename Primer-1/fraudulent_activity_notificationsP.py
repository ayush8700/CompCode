#!/bin/python3

import math
import os
import random
import re
import sys
import statistics

def activityNotifications(expenditure, d):
    noti = 0
    medList = []
    for i in range(d, len(expenditure)):
        med = statistics.median(expenditure[i-d: i])
        medList.append(med)
    j=0
    for i in range(d, len(expenditure), d):
        if expenditure[i] >= 2*medList[j]:
            noti += 1
        j+=1

    return noti
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()

