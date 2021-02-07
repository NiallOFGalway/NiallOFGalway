# Lab3.2.1-round.py
# Author: Niall O Flaherty
# This program takes in a float (number with decimal places) and outputs an integer (whole number)
# This program rounds to the nearest whole number, so not to be used where accuracy is vital

numberToRound = float(input("Enter a float number: "))
roundedNumber = round(numberToRound)

print ('{} rounded is {}'.format(numberToRound,roundedNumber))
