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


#  .tell gives an integer value when file is a binary file and returns an opaque number in case of text file
#  .seek takes two arguments offset and whence. In case of binary file whence has an integer value 0,1 or 2
#  indicating the beginning, current and ending position in the file. In case of text file whence only allows 
#  value 0 and only in extreme case takes value 2( seek(0,2) for end of file ) and offset can only take value returned by .tell

# Note:- While writing to a binary file we cannot write string it has to be
#in byte like format.This can be achieved by writing 'b' in front of string
#  Example:- b"this binary coded format"

#  Writing/Reading from a binary file 
with open('demo.txt', 'rb+') as file:
    txt=b'This is {number} line'
    for i in range(1,6):
        file.write(txt.format(number=i).encode())
    file.seek(0, 0)
    print(file.read().decode())
