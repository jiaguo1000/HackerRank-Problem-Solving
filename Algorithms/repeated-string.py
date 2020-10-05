#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    if len(s)==0 or 'a' not in s:
        return(0)

    num_rep = math.floor(n/len(s))
    num_rem = n%len(s)
    num_a_1 = len([x for x in s if x=='a'])*num_rep
    num_a_2 = len([x for x in s[:num_rem] if x=='a'])
    return(num_a_1+num_a_2)
