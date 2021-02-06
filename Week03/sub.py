# sub.py
# Author: Niall O Flaherty
# This program asks you to input 2 numbers and subtracts the 2nd number from the 1st

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
# We must use int as we are using mathematical equations. If we did not use int, the input would be treated as a string

answer = x-y
print("{} minus {} is {}".format(x,y,answer))

# QUESTION FROM LAB SHEET: When the program is running, try entering in something that is not an int eg 1.1 or hello
# ANSWER: This will cause an error as int only allows whole numbers. If you wanted to use a decimal place, you would use float