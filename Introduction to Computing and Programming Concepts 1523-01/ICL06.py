"""
Program: ICL06.py
Author: Xai Cheng
Date: 10/16/23
Purpose: Expanded from ICL05 implementing functions 
"""

import math # imported for as needed use
import random # imported for as needed use
from datetime import datetime # used to seed random variable

# quick overview of the while structure

# lets iterate over a randomly generated list

# generate the list 
l = [] # declare the list

"""
Introduce follow-on search recall the lost person in the grid, we introduce 
two dimensional lists
"""

# first initialize a grid of 0's
g = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


def locateTarget(g):
    #randomly select a location for victim
    x = random.randint(3,17)
    y = random.randint(3,17)

    #now set the victim's location
    g[x][y] = 100
    #now the area around the point

    #inner ring
    i = x - 1
    j = y - 1
    for k in range(j, j + 3):
        for l in range(i, i +3):
            if g[l][k] == 0:
                g[l][k] = 90

    #outer ring
    i = x - 2
    j = y - 2
    for k in range(j, j + 5):
        for l in range(i, i + 5):
            if g[l][k] == 0:
                g[l][k] = 80

locateTarget(g)

i = 0
while i < len(g):
    print(g[i])
    i += 1

#find target
def findTarget(g):
    #retrieve cols and rows of sgrid array
    rows = len(g)
    cols = len(g)
    tareaFound = False

    while tareaFound == False:
        #generate a random number in x and y direction
        x = random.randint(0, rows - 1)
        y = random.randint(0, cols - 1)
        #if we hit the mark stop and return it
        if g[x][y] == 100:
            return x, y
        #keep searching until we get close
        if g[x][y] != 0:
            tareaFound = True

    #inner ring
    if g[x][y] == 90:
        i = x - 1
        j = y - 1
        for k in range(j, j + 3):
            for l in range(i, i + 3):
                if g[l][k] == 100:
                    return l, k

    #outer ring
    if g[x][y] == 80:
        i = x - 2
        j = y - 2
        for k in range(j, j + 5):
            for l in range(i, i + 5):
                if g[l][k] == 100:
                    return l, k

print(findTarget(g))

