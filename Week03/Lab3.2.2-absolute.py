# Lab3.2.2-absolute.py
# Author: Niall O Flaherty
# This program takes in a number and gives its absolute value
# We are setting the input as a float as the question does not specify if the input value will be a whole number
# or have a decimal place

number = float(input("Enter a number: "))
absoluteValue = abs(number)

print('The absolute value of {} is: {}'.format(number,absoluteValue))
