"""
Program: ICL05.py
Author: Xai
Date: 10/9/23
Purpose: Brief review of repetition structures and intro to functions.
"""

import math # imported for as needed use
import random # imported for as needed use
from datetime import datetime # used to seed random variable

# quick overview of the while structure

# lets iterate over a randomly generated list

# generate the list 
l = [] # declare the list

#seed random number generator
random.seed(datetime.now().timestamp())

#lets user us a for "iterator" to populate it
for i in range(0,10000):
    l.append(random.randint(0,10000))
    
print(f'The length of l is: {len(l)}')


#just a quick reminder on the range function.
ll = range(0,130)

for i in range (0,10):
    print(ll[i])

#so no a bit of review of using the "while" structure
i =0
loavg = 0
locount = 0
lsum = 0
hicount = 0
hsum = 0

while (i < len(l)):
    if (l[i] < 5000):
        locount += 1
        lsum += l[i]
        i += 1
    else:
        hicount += 1
        hsum += l[i]
        i += 1
print(f'Low Average: {lsum/locount:10.2f}')
print(f'High Average: {hsum/hicount:10.2f}')


"""
Introduce follow-on search recall the lost person in the grid, we introduce 
two dimensional lists
"""

# first initialize a grid of 0's
sgrid = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
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


#print it out just to make sure we have a 2d array
i = 0
while i < len(sgrid):
    print(sgrid[i])
    i += 1
#now randomly select a location for the victim
x = random.randint(0,20)
y = random.randint(0,20)

#now set the victim's location
sgrid[x][y] = 100
i = 0
while i < len(sgrid):
    print(sgrid[i])
    i += 1

# retrieve cols and rows of sgrid array
rows = len(sgrid)
cols = len(sgrid[0])

"""
# now lets search for the 100
i = 0
j = 0
while i < rows:
    j = 0
    while j < cols:
        if sgrid[i][j]j == 100
            print (f'100 was found at {i:5d} , {j:5d}')
            break
        j += 1
    i += 1
"""

#implement in class code
ffind = True
row = 0
col = 0
#implement a while loop base search
while sgrid[row][col] != 100:
    if col < 19:
      col = col + 1
    else:
        col = 0
        row = row + 1
        if row < 19:
            ffind = False
if ffind:
    print(f'100 was at {row:5d} , {col:5d}')
else:
    print("Party no found")
                 


