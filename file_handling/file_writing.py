#  Writing to a file in Python

import os

write = "This a test to truncate a file\n"  #string to be written
path = 'write.test'                         #path of the file
if os.path.exists(path):
    try:
        file = open(path,"w+") #opening a file in read write mode along with truncation
        print(file.read())
        file.write(write)  #Note:- cursor moves to the end of file after writing to it
        file.seek(0)       #moving the cursor to the beginning of a file
        print(file.read())
        file.close()
    except Exceptions:
        print("something went wrong")
    finally:
        print("Checking for proper handling of file: {}".format(file.closed))
else:
    print("Error encountered while opening a file ):")


#  writing the same code using 'with'-'as' block
print("\nRepeating the operation using 'with'-'as' block")
if os.path.exists(path):
    try:
        with open(path,"a+") as file:
            print(file.read())
            file.write(write)#Note:- cursor moves to the end of file after writing 
            file.seek(0)     #moving the cursor to the beginning of a file
            print(file.read())
    except Exceptions:
        print("Something went wrong ):")
    finally:
        print("Checking for proper handling of file {}".format(file.closed))
else:
    print("Error encountered while opening a file ):")
