#######
# File: Homework1_drb160130.py
# Author: Dorian Benitez (drb160130)
# Date: 8/28/2020
# Purpose: CS 4395.001 - Homework #1 (Text Processing with Python)
#######

import sys
import pathlib
import re
import pickle


# Step 3: Define a Person class with fields last, first, mi, id, and phone
class Person:
    def __init__(self, last, first, mi, id, phone):
        self.last = last
        self.first = first
        self.mi = mi
        self.id = id
        self.phone = phone

    # Step 3: Create a display() method to output fields as shown in the sample run
    def display(self):
        print('Employee id: ', self.id)
        print('\t', self.first, ' ', self.mi, ' ', self.last)
        print('\t', self.phone, '\n')


# Step 4: Create a function to process the input file.
def process_lines(persons):
    # Step 2: The user needs to specify the relative path ‘data/data.csv’ in a sysarg.
    #         If the user does not specify a sysarg, print an error message and end the program
    if len(sys.argv) < 2:
        print('Please enter a filename as a system arg')
        quit()

    #  Read the file
    f = open(pathlib.Path.cwd().joinpath(sys.argv[1]), 'r')
    line = f.readline()  # Remove the heading line of the CSV file

    while True:
        line = f.readline().strip()
        if not line:
            break
        temp_list = line.split(',')  # Split on comma to get the fields as text variables

        # Modify last name and first name to be in capital case
        temp_list[0] = temp_list[0].capitalize()
        temp_list[1] = temp_list[1].capitalize()

        # Modify middle initial to be a single upper case letter. Use ‘X’ as a middle initial if one is missing.
        if len(temp_list[2]) != 1:
            temp_list[2] = 'X'

        # Modify id using regex, if necessary
        while re.match('[A-Za-z][A-Za-z]\d{4}', temp_list[3]) is None:
            print('ID invalid: ', temp_list[3])
            print('ID is two letters followed by 4 digits')
            temp_list[3] = input('Please enter a valid id: ')

        # Modify phone number, if necessary
        while re.match('\w{3}-\w{3}-\w{4}', temp_list[4]) is None:
            print('Phone ', temp_list[4], ' is invalid')
            print('Enter phone number in form 123-456-7890')
            temp_list[4] = input('Enter phone number: ')

        # Create a Person object and save the object to a dict of persons, where id is the key.
        person = Person(temp_list[0], temp_list[1], temp_list[2].capitalize(), temp_list[3], temp_list[4])
        persons[temp_list[3]] = person

    return persons  # Return the dict of persons to the main function.


# Main function
if __name__ == '__main__':
    employees = {}
    employees = process_lines(employees)

    # In the main function, save the dictionary as a pickle file
    pickle.dump(employees, open('employees.pickle', 'wb'))
    employees_in = pickle.load(open('employees.pickle', 'rb'))  # Open the pickle file for reading

    # Print each person using the Person display() method to verifiy that the pickle was "unpickled" correctly
    print('\nEmployee list:\n')
    for emp_id in employees_in.keys():
        employees_in[emp_id].display()
