import os

#  For program to work as intended a file needs to created in the same folder as the 
#  file_detection.py labelled 'test.log'(it may or maynot be empty file) , also folder
#  containing the subfolder(folder in which this file exits) must also have 'list' as 
#  its subfolder

path = 'test.log'
path1 = '..//lists'

if os.path.exists(path1):
    print("location exists")
    if os.path.isfile(path1):
        print("A file is detected")
    elif os.path.isdir(path1):
        print("A folder is detected")
else:
    print("path does not exist: {}".format(path1))

