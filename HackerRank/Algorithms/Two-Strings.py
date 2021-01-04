#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    d1 = dict()
    for i in s1:
        d1[i] = 1

    flag = 0
    for j in s2:
        if j in d1:
            flag = 1
            return('YES')
    
    if flag==0:
        return('NO')

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()

