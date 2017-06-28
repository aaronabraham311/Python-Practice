name = raw_input ("Please enter your full name, with proper capitalization: ") # Getting user's full name

print ("Your initals are: ")

for i in name: # Will output capital letters, which are initials
    if i.isupper() == True:
       print ("%s." %(i)),

