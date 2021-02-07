# Lab3.2.4-convert.py
# Author: Niall O Flaherty
# This program takes in a float number (decimals) and outputs the number as an absolute

floatNumber = float(input("Please enter an amount: "))
# Use FLOAT as there is a decimal input

absolute = abs(floatNumber)

absoloteNoDecimal = int(absolute * 100)
# This moves the decimal to the right by 2 places ie. 5.99 would change to 599

print('The amount in cent is: {}'.format(absoloteNoDecimal))