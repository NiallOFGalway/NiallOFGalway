# randomGenerator.py
# Author: Niall O Flaherty
# This program prints out a random number between 1 and 10

# import random
# number = random.randint(1,10)
# print("Here is a random number between 1 and 10: {}".format(number))


first = int(input("Enter first number "))
last = int(input("Enter last number "))

import random
number = random.randint(first,last)
print("Here is a random number between {} and {} is {}".format(first,last,number))
# This allows the user to input the 2 numbers in which the program will output a random number between these numbers