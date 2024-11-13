"""
Program: ICL06.py
Author: Xai Cheng
Date: 10/23/23
Purpose: Introduce at a elementary level file access, both read and write. Use
data access to introduce string manipulation.
"""
import math # imported for as needed use
import random # imported for as needed use
from datetime import datetime # used to seed random variable

#lets read a file, we do this four ways
#1. create a file object
#2. Call member methods on the object to read the file into:
#   1. One large string
#   2. A list of lines
#   3. A slingle line
#   4. Iterate over the file using a "for"

#Create a file object that relates a file to an object in our script

f = open("FoodValues.txt","r")

#create an output file
fo = open("Elements.txt","w")

#read into a large string
s = f.read()
print(s)
#read into a single line
#l = f.readline()
#while (l != ''):
#    print(l)
#    l = f.readline()
#read the file into a list
#fl = f.readlines()
#print(fl)
#for l in f:
#    print(l)

for l in fl:
    ol = l[0:5]
    fo.writeline(ol)

f.close(f)
fo.close(fo)
