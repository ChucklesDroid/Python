#  scope :- a variable is only recognized in a given region
         #  a variable is only available from inside the region it is created 
         #  a global and locally scoped versions of the variable can be created

#  Note:- Python makes use of LEGB rule( local, enclosing, global, built-in ) to access
#  variables

name = "aakarsh"    #global variable 

def foo():
    name = "foo"    #local variable
    print(name)     #prints local variable

foo()
print(name)         #prints global variable
