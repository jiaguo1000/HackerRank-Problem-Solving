#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    output_set = {}
    for i in ar:
        if i not in output_set:
            output_set[i] = 1
        elif i in output_set:
            output_set[i] += 1
    
    output_list = [math.floor(x/2) for x in output_set.values()]
    output = sum(output_list)
    return(output)
