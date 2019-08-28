#!/bin/python3

import os
import sys

def timeConversion(s):
    hour, mt, secT = s.split(':')
    sec = secT[:2]
    T = secT[2:]

    if (int(hour)>=0 and int(hour)<=11 and T=='PM'):
        hour = str(int(hour)+12)
    elif (int(hour)==12 and T=='AM'):
        hour = '00'
    return f'{hour}:{mt}:{sec}'

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

