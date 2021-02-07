# Lab3.1.3-div.py
# Author: Niall O Flaherty
# This program asks you to input 2 numbers and divides the first number by the 2nd number
# Outputs the integer result and remainder

x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))

answer = int(x//y)
# This divides the integers entered

remainder = x%y 
# This gives the remainder

print("{} divided by {} is {} with remainder {}".format(x,y,answer,remainder))
