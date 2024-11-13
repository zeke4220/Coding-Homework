"""
Program:ICL10.py
Author: Xai Cheng
Date: 11/20/23
Purpose: Introduce calsses and inheritance
"""

# we define a class using a class definition, line 9
class Seat:
    # functions we wish to be a part of a Seat object are defined here
    # the init function is a special function which executes each time
    # an object of the Seat type is created.
    
    def __init__(self):
        # this is an instantiator or constructor fuction which is
        # executed whenever an object is created.
        self.first_name = ''
        self.last_name = ''
        self.paid = 0.0
        
    def reserve(self, f_name, l_name, amt_paid):
        self.first_name = f_name
        self.last_name = l_name
        self.paid = amt_paid

    def make_empty(self):
        self.first_name = ''
        self.last_name = ''
        self.paid = 0.0

    def is_empty(self):
        return self.first_name == ''

    def print_seat(self):
        print(f'{self.first_name} {self.last_name}, Paid: {self.paid:.2f}')

# functions that recieves a list of seat objects, seats, and empties them
def make_seat_empty(seat):
    for s in seats:
        s.make_empty()


# functions that prints the content of a list of seats
def print_seats(seat):
    for i in range(len(seats)):
        print(f'{i}:', end='')
        seats[i].print_seat

num_seats = 5

available_seats = []
for i in  range(num_seats):
    available_seats.append(Seat()) #create a list of reference to Seat object

"""
command = input('Enter command (p/r/q):\n')
while command != 'q':
    if command == 'p': # Print seats
        print_seats(available_seats)
    elif command == 'r': # Reserve a seat
        seat_num = int(input('Enter seat num:\n'))
        if not available_seats[seat_num].is_empty():
            print('Seat not empty')
        else: # assign a seat
            fname = input('Enter first name:\n')
            lname = input('Enter last name:\n')
            paid = float(input('Enter amount paid:\n'))
            available_seats[seat_num].reserve(fname, lname, paid)
    else:
        print('Invalid command.')

    command = input('Enter command (p/r/q):\n')

"""
mystr = 'text'
print('text'.upper())
    
