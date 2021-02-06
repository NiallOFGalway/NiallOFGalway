# randomFruit.py
# Author: Niall O Flaherty
# This program outputs a random fruit

import random

fruits = ['Apple', 'Banana', 'Mango', 'Pear']

index = random.randint(0,len(fruits)-1)

fruit = fruits[index]
print("A Random fruit is: {}".format(fruit))
