#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    def tempSum(x):
        return(sum(x[0])+x[1][1]+sum(x[2]))
    
    output = tempSum([x[0:3] for x in arr[0:3]])
    for i in range(4):
        for j in range(4):
            temp = tempSum([x[j:j+3] for x in arr[i:i+3]])
            if temp > output:
                output = temp
    
    return(output)
