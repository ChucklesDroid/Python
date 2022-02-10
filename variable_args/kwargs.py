#  **kwargs :-   variable argument list for a given function. kwargs is the shorthand 
                #  for keyword arguments. 'kwargs' is not that important it can be 
                #  replaced with any variable , its just a naming convention. 
                #  Although '**' is very important

                #  Its basically a parameter that will pack all arguments into a 
                #  dictionary

                #  Its similar to *args in functionality but different from it in the
                #  sense that it make use of keyword arguments where as *args makes use
                #  of positional arguments

#  A simple function which accesses key-value pairs in the dictionary
def hello( **kwargs ):
    print("Hello " + kwargs['first'] + " " + kwargs['second'])

#  We can make use 'captions' instead of 'kwargs'
def foo( **captions ):
    print("Hello ", end="")
    for key,value in captions.items():
        print(value, end=" ")

hello(first="Aakarsh", second="MJ")
foo(title = "Mr.", first_name = "Aakarsh", last_name = "MJ")

