# Lab3.2.3-floor.py
# Author: Niall O Flaherty
# This program takes in a float number and outputs an integer (int) rounded down
# We need to use the math module math.floor() - w3schools

import math

numberToFloor = float(input("Enter a float number: "))
flooredNumber = math.floor(numberToFloor)

print('{} floored is: {}'.format(numberToFloor,flooredNumber))
