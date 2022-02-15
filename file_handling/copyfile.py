#  To copy a file we make use of 'shutil' module and related functions:-

#  copyfile(src,dest,follow_symlinks="True") src is the source path, dest is the dest path,
#  The third argument 'follow_symlinks' is optional and is a keyword argument .By default 
#  True, if the value is False then source represents a symbolic link and destination will be 
#  created as a symbolic link
#  All three functions have same argument list

#  shutil.copyfile() :- copy contents of the file, metadata is not copied, source and 
#  dest must be a file , if file exists then it will be truncated otherwise new file is 
#  created if file does not exist

#  shutil.copy() :- shutil.copyfile() + dest can be a folder(src must be a file) + preservses
#  file permissions

#  shutil.copy2() :- shutil.copy() + copies metadata of the file such as last modified, date 
#  created 
#  Note:- If src and dest have same path then it would report a error

import shutil                                #For copying files
import os                                    #For checking file permissions

src = 'write.test'
dest1 = 'write(copy1).test'
dest2 = 'write(copy2).test'
dest3 = 'write(copy3).test'

print("Permissions: ",os.stat(src).st_mode)  #Displaying file permissions
shutil.copyfile(src,dest1)
print("Permissions: ",os.stat(dest1).st_mode)#Displaying file permissions 
shutil.copy(src,dest2)
print("Permissions: ",os.stat(dest2).st_mode)#Displaying file permissions 
shutil.copy2(src,dest3)
print("Permissions: ",os.stat(dest3).st_mode)#Displaying file permissions 

#  copying a file by specifying the directory only
shutil.copy(src,"..")                        #Creates a file with same name as src path file
print(os.listdir(".."))
