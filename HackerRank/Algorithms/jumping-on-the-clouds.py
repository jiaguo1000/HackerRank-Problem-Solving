#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    output = []
    curr = 0
    while curr < len(c)-2:
        if c[curr+2] == 0:
            output.append(curr+2)
            curr += 2
        elif c[curr+2] == 1 and c[curr+1] == 0:
            output.append(curr+1)
            curr += 1
    
    if curr == len(c)-1:
        return(len(output))
    elif curr == len(c)-2:
        return(len(output)+1)
