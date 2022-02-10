#  Exception   :- Errors detected during execution of a program that interupt the flow
               #  of program
#  Exceptions are basically events detected during run time that interrupt the flow of
#  programs

#  x = int(input( "Enter operand 1: " ))
#  y = int(input( "Enter operand 2: " ))

#  print(x/y)

#  Its very much possible for user to enter 0 in 2nd input or enter a string instead
#  of numerical value. It can face anyother issues as well
#  To take care of that we will make use of 'try' block - to look for any runtime 
#  errors in the code block and succesively make use of except to print a message for
#  the errors encountered. We can even make use of 'as' to print the exact message
#  and at the end make use of 'finally' to execute a block of code regardless of it 
#  encountering a error or not

try:
    x = int(input( "Enter operand 1: " ))
    y = int(input( "Enter operand 2: " ))
    z = x/y
except ZeroDivisionError as e:
    print("Error encountered: {}".format(e))    
    print("Mathematically division by zero is not defined")
except Exception :
    print("Something went wrong :(")
else:
    print(z)
finally:
    print("Operation completed")

#  Its not good practice to have a single exception block to handle all exceptions but
#  have multiple exception blocks which will handle the specific errors first 

#  finally will print message regardless an exception is caught or not. Its present 
#  towards the end. (Useful in File handling)
#  else here will execute the block of message if no error occurs



