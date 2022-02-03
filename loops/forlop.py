#  A for loop is used for iterating over a sequence (that is either a list,
#  a tuple, a dictionary, a set, or a string).
#  This is less like the for keyword in other programming languages, and works
#  more like an iterator method as found in other object-orientated 
#  programming languages

#  name = "aakarsh"
#  for x in name:
    #  print(x)

#  #  Looping through a string
#  for x in "banana":
    #  print(x)

#  #  Break statement
#  for x in "banana":
    #  if x=="n":
        #  break
    #  else:
        #  print("Left the chat")

#  #  Continue Statement
#  for x in "banana":
    #  if( x == "n" ):
        #  continue
    #  else:
        #  print(x)
        

#  Range statement in for loop
#  Syntax :- range(start:end:step)
#  for x in range(2,5)
    #  print(x)

#  for x in range(5): #represents values from 0 to 5
    #  print(x)

#  for x in range(0,20,5):
    #  print(x)
    
#  Else in for loop
#  for x in range(10):
    #  if x == 5:
        #  break
    #  else:
        #  print(x)
#  else:
    #  print("loop completed")

#  Nested Loops 
#  Printing 2D array
#  for x in range(5):
    #  for y in range(5):
        #  print(x,y)

#  for loops cannot be empty, but if you for some reason have a for loop 
#  with no content, put in the pass statement to avoid getting an error.

#  for x in [0,2,4]:
    #  pass
#  else:
    #  print("Empty for loop printed")
#  #  Alternative method
#  for x in range(5):
    #  if x == 3:
        #  pass
    #  else: 
        #  print(x)

#  Using for loop and time module to print Happy New Year
#  importing time module
import time
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1) # 1 indicates that it will sleep for 1s
else:
    print("Happy New Year")
