# Importing library for square root function
import math

# Getting input from user
firstLength = input("Please input one side of the triangle: ")
hypotenuse = input("Please input the hypotenuse of the triangle: ")

# Converting to integers
int(firstLength)
int(hypotenuse)

secondLength = math.sqrt((hypotenuse ** 2) - (firstLength ** 2)) # Calculation

print ('The length of the missing side is: %s' %(secondLength)) # Output