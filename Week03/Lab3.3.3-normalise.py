# Lab3.3.3-normalise.py
# Author: Niall O Flaherty
# This program reads in a string, strips all leading and trailing spaces and converts the string to lower case

inputString = input("Enter a string: ")
normaliseString = inputString.strip().lower()

lengthOfinputString = len(inputString)
lengthofnormaliseString = len(normaliseString)

print("The String normalised is: {}".format(normaliseString))
print("We reduced the input from {} to {} characters".format(lengthOfinputString,lengthofnormaliseString))