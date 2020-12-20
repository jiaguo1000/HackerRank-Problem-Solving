#!/bin/python3

import math
import os
import random
import re
import sys

class QueueEntry: 
    def __init__(self, v = 0, dist = 0): 
        self.v = v 
        self.dist = dist 

# Complete the quickestWayUp function below.
def quickestWayUp(ladders, snakes):
    N = 100
    moves = [-1] * N
    visited = [False] * N
    ladders_new = [[x[0]-1, x[1]-1] for x in ladders]
    snakes_new = [[x[0]-1, x[1]-1] for x in snakes]

    for L in (ladders_new, snakes_new):
        for l in L:
            moves[l[0]] = l[1]

    queue = []
    visited[0] = True
    queue.append(QueueEntry(0, 0))
    qe = QueueEntry() # A queue entry (qe)
    while queue:
        qe = queue.pop(0)
        if qe.v == N - 1: 
            break
        
        j = qe.v+1
        while j <= qe.v + 6 and j < N:
            if visited[j] is False:
                temp = QueueEntry() 
                temp.dist = qe.dist + 1
                visited[j] = True
                temp.v = moves[j] if moves[j] != -1 else j
                queue.append(temp) 
            j += 1

    if qe.v == N-1:
        return(qe.dist)
    else:
        return(-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        fptr.write(str(result) + '\n')

    fptr.close()
