"""
Program: ICL02
Author: Xai Cheng
Date: 9/11/23
Purpose: Calculate energy to move a block up an incline
"""
#needed for math of the angle of slope
import math

#initial conditions
m = 40 #mass of block 40kg
slope = 40 #degree of the slope
d = 100 #distance of 100 meters
g = 9.8 #accerelation of gravity 9.8 meters per second squared

#Calculateion step

#Calculate radians in 40 degrees
rads = (slope * 2 * math.pi) / 360

#Calculate force of friction
ff = m * g * math.cos(rads)

#Calculate Force
f = m * g * math.sin(rads)

#Calculate total force
f = f + ff

#Calulate the work
w = f * d

#Present the result
print("Work done:", w, " jouels")
