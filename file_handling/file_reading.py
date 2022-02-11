#  Opening the file for reading purposes 

file = open("test.log","r")
#  print(file.read())      #.read() returns the entire read file
#  We can give optional argument size to indicate bytes of data to be read
print(file.read(4))         #Reads 4 bytes of data from the file

print(file.closed)      #checks if the file is opened or closed
file.close()            #closes the file since its open

#  To read the file line by line
file = open("test.log", "r")
print(file.readline())  #It also takes an additional argument 'size' similar to read
                        # but more specific to reading bytes from a line rather than 
                        # whole file
file.close()            #Closing the file
print(file.closed)


#  By making use of 'with' and 'as' keywords we do not have to close the file each time
#  rather they are closed automatically

#  'as' keyword in itself is used to create alias, with a file and with a except clause
#  'with' statement is a control flow structure whose basic structure is :-
#  'with' - 'as' block helps in error detection using try-except blocks
#  with expression [as variable]:
    #  with-block
with open("test.log") as file:
    print(file.read(4))
print(file.closed)    #File is closed automatically by using 'with' 'as' control block

#  Error Detection
try:
    with open("test.lg") as file:
        print(file.read())
except FileNotFoundError as e:
    print("Error encountered: {}", e)
except Exceptions:
    print("Something went wrong ):")
finally:
    print("End of program is reached")
