#  Importing os to move files

import os                   #for os.replace(src, dest) and os.path.exists

src = 'mv.test'             #path of the source file 
dest = r'..'                #path of the destionation file
try:                        #try block
    if os.path.exists(dest) and os.path.isfile(dest):
        print("file already exists")
    elif not(os.path.exists(src)):
        print("{} :does not exist".format(src))
    else:
        os.replace(src,dest)
        print('file moved')
except FileNotFoundError:   #file not found error
        print("Error encounted: File not found-{}".format(src))
except Exception as e:
        print("Error detected: {}".format(e))
        print("Something went wrong ):")
finally:
        print("Program executed")
