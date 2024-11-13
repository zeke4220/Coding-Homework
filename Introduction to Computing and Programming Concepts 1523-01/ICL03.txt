"""
Program: ICL03.py
Author: Xai Cheng
Date: 9/18/2023
Purpose: This program exercise types, modules and if states as if review of
		Python.
"""

"""
import math #import math for calculations
import random #to generate random numbers

#lets get a little loose with a quick calculation of calorie burned in exercise

age = float(input('Enter your age:'))
height = float(input('Enter your weight(lbs):'))
heart_rate = float(input('Enter your training heartrate(bpm):'))
time = float(input('Enter your training time(min):'))
cal_lb = 3500 #calories per pound
 
#calculate calories
cal = (age * 0.2757 + weight * 0.03395 + hr * 1.0781 - 75.4891) * time / 8.368
 
#calculate lbs of fat comsumed.
lbsfat = cal / cal_lb
 
#presentation i.e. output
print("Calories used: ",f"{cal:.2f}")
print("Pounds fat burned: ",f"{lbsfat:.4f}")
"""
"""
#datatypes
    #String
    #list
    #tuple
    #set

#Strings -- immutable
s = 'this is a string'
print("Id of s", id(s))
#get len
print("Length of s: ", len(s))
s1 = "this is also a string"
s = s + s1 #concatenate s and s1
print("Length of s: ", len(s))
print("Concatenated s id", id(s))

#lets get object ids
print("Plain s1: ", id(s1))
print("id of literal s1", id(" this is also a string"))

print(" this is also a string".capitalize())
"""

#introduce lists
l = [] #create an empty list
#add a member to the list
l.append(5)
l.append(8)
l.append(13)
print(l)

#pop a value off of l
print(l.pop())

#remove a value by contents
l.remove(5)
print(l)