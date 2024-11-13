''''
Program: ICL11.py
Author: Xai Cheng
Date: 11/27/23
Purpose:
1. Introduce recursion as an algorithmic technique
2. Demonstrate recursion as a mechanical technique utilizing the stack
3. Implement a few examples whithin
'''

#import the usual
import math
import random
import string
import time

# implement in code

# our initialization

sv = int(input('Enter integer to search for: '))
i = 0
il = [1, 5, 65, 33, 3, 25,  4, 11, 30, 22]
foundVal = False
# now the algorithm
while (i < len(il)):
    if il[i] == sv:
        foundVal = True
        break
    i += 1
# now present results
if foundVal:
    print(f'Value {sv} found at {i}')
else:
    print(f'Value {sv} not in the list')


def findval(i,sv, il):
    if i == len(il):
        return -1
    elif il[i] == sv:
        return i
    else:
        return findval(i+1, sv, il)
    
sv = int(input('Enter integer to search for: '))
i = 0
il = [1, 5, 65, 33, 3, 25,  4, 11, 30, 22]
ivar = findval(i, sv, il)
if ivar == -1:
    print(f'Value {sv} is not in the list')
else:
    print(f'Value {sv} found at index {ivar} of list')


start_time = time.time()
i = 0
il = []
while i < 10000:
    il.append(random.randint(0, 100000))
    i += 1
end_time = time.time()
print(f'Time to create the list: {end_time - start_time}')

# sort our list
il.sort()

# now lets search linearly to determine if a randomly generated value is
# in the list

# perform 5000 linear searches
matches = 0
start_linear = time.time()
for i in range(5000):
    # gen random number
    sv = random.randint(0, 10000)
    for j in il:
        if j == sv:
            matches += 1
end_linear = time.time()

# perform 5000 binary searches

# first define a binary search function

def binary_search(il, sv):
    low = 0
    high = len(il) - 1

    while low <= high:
        #finding the id using floor division
        mid = low + ((high - low) // 2)

        #target value is present at the middle of the array
        if il[mid] == sv:
            return mid
        
        #target value is present in the low subarray
        elif sv < il[mid]:
            high = mid - 1

        #target value is present in the high subarrray
        elif sv > il[mid]:
            low = mid + 1

    #target value is not present in the array
    return -1

#perform 5000 binary searches
matches = 0
start_binary = time.time()
for i in range(5000):
    #gen random number
    sv = random.randint(0, 10000)
    r = binary_search(il, sv)
    if r != -1:
        matches += 1
end_binary = time.time()

print(f'Linear search time: {end_linear - start_linear}')
print(f'Binary search time: {end_binary - start_binary}')

import math

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Allocates a new node with given data
def newNode(data):
    new_node = Node(data)
    new_node.data = data
    new_node.next = None
    return new_node

# Function to insert a new node at 
# end of linked list using recursion.
def insertEnd(head, data):