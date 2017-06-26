# Getting input
number = input("Please enter a 4 digit number: ")

# Performing calculations
thousands = (number % 10000) / 1000
hundreds = (number % 1000) / 100
tens = (number % 100) / 10
ones = number % 10

# Outputting digits of numbers
print ("The thousands digit is: %s" %(thousands))
print ("The hundreds digit is: %s" %(hundreds))
print ("The tens digit is: %s" %(tens))
print ("The ones digit is: %s" %(ones))