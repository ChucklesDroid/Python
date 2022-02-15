# To move a file in python we make use of os module

import os                   #For moving a file

src = 'mv.test'
dest = r'../mv.test'
#  Writing the code in try-except block
#  First moving a file 
try:
    if os.path.exists(dest):
        print("file already exists")
    else:
        os.replace(src,dest)
        print(src + " moved")
except FileNotFoundError:
    print(src + " not found")
except Exception:
    print("Something went wrong")
else:
    print("No errors encountered")

#  Moving a folder in python 
src1 = 'testfldr'
dest1 = r'../testfldr'
try:
    if os.path.exists(dest1):
        print("Folder already exists")
    else:
        os.replace(src1,dest1)
        print(src1 + " moved successfully")
except FileNotFoundError:
    print(src1 + " not found")
except Exception as e:
    print("Error encountered:{}".format(e))
    print("Something went wrong (:")
else:
    print("No errors encountered")
