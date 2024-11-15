"""
Program: ICL09
Author: Xai Cheng
Date: 11/13/23
Purpose:
1. Exception handling
2. Module use
3. Large file usage with both modules and exceptin handling
"""

import math # imported for as needed use
import random # imported for as needed use
from datetime import datetime # used to seed random variable

"""
Exception: an object that is created by the execution enviroment when
an error is detected at the execution time.

These errors are found within an "except" block and appropriate
is raised.

Execptions are defined by the Python enviroment and can be custom develped
as a class definition by the developer(s).

Examples of the built-in exceptioons are:
    1. Exception - base class for all exceptions
    2. NameError - raised when a variable reference does not exist
    3. ZeroDivisionError - raised when the second argument to a division
       operator is 0
    4. OverFlowError -  raised when results of an arithmetic operator is too
       large
    5. ValueError - raised 
    
    
    
    
Exceptions can also be defined by the programmer to sit a particular
application they are working on.

Example the use of a try-except structure in Python
"""
"""
l = [1, 45, 32, 67, 87, 23]
q = input('Input index or \'q\' to quit: ')
while q != 'q':
    try:
        d = input('Enter divisor: ')
        d1 = int(d)
        index = int(q)
        result = l[index] / d1
        print('The result is: ', result)
        raise IOError
    except IndexError:
        print('Index was out of range')
    except ValueError:
        print('Index entered not valid type')
    except ZeroDivisionError:
        print('Divisor entered was 0')
    except Exception:
        print('Exception thrown on data entry or conversion')
    q = input('Input index or \'q\' to quit: ')

"""
"""
Moduless:

Module is simply a script file that containsfunctions, constant that
can be used by other Python scripts.

Three trypes of modules:
1. Modules that come standard with the Python interpreter
   Example: math, random, etc.
2. Modules that are developed by other parties andmust be installed
   outside repositories, etc
3. Custom modules which are created by the developer which can be
   a particular project

We gain access to the functions and constants in module by importing
into our script.

There are 2 basic way to import a module to a script:

1. import <module> which imports the module fuctions inot the system
of out executing script. They are accessed by using the module name
dot operator and spcific function or constant we wish to use.

2. from <module> import func1, func2. This allows the script to call
function directly without using the module name

Modules are stored in directories

1. The system modules and some that are added are in the system
directory the location of which varies.

2. In an assigned directory often accesed using the PYTHONPATH variables

3. With small projects in the local directory of the script se are using

Any Python script can be imported as a module to a script. to


script and imprted module a reserved word, __name__ will be



"""



"""
#let exercise the use of functions

import ICL09Module

def main():
    #calculate area of circle
    r = float(input('Input radius of circle: '))
    a = ICL09Module.circleArea(r)
    print(f'Area of circle: {a:8.2f}\n')
    b = float(input('Base of rectangle:'))
    h = float(input('Height of rectangle:'))
    print(f'Aread of rectangle: {ICL09Module.rectArea(b,h):8.2f}\n')
    b = float(input('Base of triangle:'))
    h = float(input('Height of triangle:'))
    print(f'Area of Triangle: {ICL09Module.triArea(b,h):8.2f}\n')

if __name__== '__main__':
    main()
"""

"""
My breakfast:
2 eggs
4oz ham
1 pc whole wheat toast
4oz Heinz Beans
8oz Orange Juice
4oz red cabbage sauerkraut
4oz pickled beets
"""

"""
Question: Using the foodvalues text files:
protein(gr), calories
carbohydrate(gr), calories
fat(gr), calories
total calories
"""


#create a file object that relates a file to an object in our script


f = open("FoodValues.txt","r")

#create an output file
fo = open("Elements.txt","w")

#read into a large string
l = f.readline()
while (l != ''):
    tl = l.split('\t')
    tl1 = tl[0:11]
    so = ''
    for s in tl1:
        so += s+'\t'
    so = so + '\n'
    fo.write(so)
    l = f.readline()

f.close()
fo.close()

