"""
Title: ICL04.py
Author: Xai Cheng
Date: 10/2/23
Purpose: Illustrate loops and ifs by finding the local in and max of a 3rd
degree polynomial: y =1.2*(x1**3) + 3.7*(x1**2) - 2.362*x1 + 7.63
between x=-5 and x=5
"""

#INITIALIZATION
#step
step_size = 0.1

#search range
x_start = -5.0
x_end = 5.0

#starting point
x1 = x_start
y1 = 1.2*(x1**3) + 3.7*(x1**2) - 2.362*x1 + 7.63

#set the initial slope value to a very large number
slope_old = 1000000000000

#now begin the loooop
while x1 < x_end:

    #add step to x1 and set x2
    x2 = x1 + step_size

    #calculate y2
    y2 = 1.2*(x2**3) + 3.7*(x2**2) - 2.362*x2 + 7.63

    #calculate the current slope
    slope_new = (y2 - y1) / (x2 - x1)

    #display the values of x1, y1 and the slope
    print(f"{x1:.2} {y1:.2} {slope_new:.2}")

    #check if one slope value is positive and the other negative
    if((slope_new > 0) and (slope_old < 0)):
        localmin = x1
    if ((slope_new < 0) and (slope_old >0)):
        localmax = x1

    #adjust to the new slope value
        slope_old = slope_new

    #now calculate the next values for x1 and y1
    x1 = x2
    y1 = 1.2*x1**3 + 3.7*x1**2 - 2.36*x1 + 7.63

#once the loop terminates, output the result
print("Local min found: ", localmin)
print("Local max found: ", localmax)
