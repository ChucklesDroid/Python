#  function :- is a block of code that is executed when it is called 
#  We make use of 'def' to define a function

#  Function Declaration
def hello():
    print("Hello")

hello()

#  Function with parameters( also shows function overloading )
def hello( name ):
    print("Hello " + name)

hello("aakarsh")

#  Function having varied argument list
def hello( first_name, last_name, age ):
    print("Hello "+ first_name+ " "+ last_name)
    print("You are "+ str(age)+ " years old!")

hello("aakarsh", "mj", 21)

