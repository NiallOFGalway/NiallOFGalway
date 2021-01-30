# addOne.py
# Author: Niall O Flaherty
# In this program, when you enter a number, the output will be that number +1
# Reference: Adrew Beatty / VIDEO:  Prog 2.2.1 First Programs

number = int(input('Enter Number'))
# This asks the user to input a number, hence INPUT. However, we must convert this to an integer
# so that it can be added below as this would not work if it remained as a string (this would be like trying to add alpha to numeric)

newNumber = number + 1
# This defines that the output will be the original number +1

print ('{} plus one is {}'.format(number,newNumber))
# This outputs the original numer + 1