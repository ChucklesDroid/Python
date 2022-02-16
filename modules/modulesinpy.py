#  modules in python is a file containing python code which may be functions 
#  , classes,etc. It is used with modular programming which is to seperate programs
#  into parts

#  import modul             # This imports user defined module

#  modul.foo(8)             # Accessing function foo defined in modul

#  #  We can even give aliases to modules in python
#  import modul as m
#  m.foo("Froppy")

#  To import only specific functions of the module
#  from modul import foo,hello
#  hello("Aakarsh")
#  foo(7)

#  To import every function in given module alternative can be 
from modul import *         # This is dangerous since functions in different module can have same name( can run into naming conflicts ) 

#  To print pre defined modules
help("modules")
