#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
import os
import math

def countInversions(x):
    if len(x)==1:
        return(x, 0)
        
    x_len = len(x)
    x0 = x[:math.ceil(x_len/2)]
    x1 = x[math.ceil(x_len/2):]
    
    x0_sort, r0 = (x0, 0) if len(x0)==1 else countInversions(x0)
    x1_sort, r1 = (x1, 0) if len(x1)==1 else countInversions(x1)
        
    y = []
    i = 0
    j = 0
    r2 = 0
    
    for k in range(x_len):
        if i<len(x0_sort) and j<len(x1_sort):
            if x0_sort[i] <= x1_sort[j]:
                y.append(x0_sort[i])
                i = i+1
            else:
                y.append(x1_sort[j])
                j = j+1
                r2 = r2 + (len(x0_sort)-i)
                
        elif i<len(x0_sort) and j>=len(x1_sort):
            y.append(x0_sort[i])
            i = i+1
        elif i>=len(x0_sort) and j<len(x1_sort):
            y.append(x1_sort[j])
            j = j+1
             
    return(y, r0+r1+r2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)[1]

        fptr.write(str(result) + '\n')

    fptr.close()

