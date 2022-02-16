#  To remove files and empty folders in python os module is reqd

import os
import shutil                       #used to delete a folder

#  src = 'rm.test'
src = 'folder'
try:
    if not(os.path.exists(src)) :
        print(src + " does not exist") 
    else:
        #  os.remove(src)           #used to delete files only
        #  os.rmdir(src)               #used to delete empty folders
        shutil.rmtree(src)          #used to delete non empty folders
except FileNotFoundError:
    print("File not found")
except IsADirectoryError:
    print("os.remove cannot delete empty folders use 'os.rmdir' to delete empty folders")
except Exception as e:
    print("Error encountered: {}".format(e))
    print("Something went wrong (:")
else:
    print("File may have been deleted since no errors encounterd")
