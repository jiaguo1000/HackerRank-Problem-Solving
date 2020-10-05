#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    cur_s = 0
    pre_s = 0
    vall = 0
    for i in path:
        if i=='U':
            cur_s += 1
        elif i=='D':
            cur_s -= 1
        
        if pre_s==0 and cur_s==-1:
            vall += 1
        pre_s = cur_s
        
    return(vall)

