#  higher order functions take either functions as arguments or return functions. Functions are basically object and can be assigned to a variable in python

#  1. using functions as variables
def usefulfunc( x, y ):
    print( x+y )

addr = usefulfunc
#  print(addr)
addr(1,2)

say = print
say("Whoa !!")

#  2.Higher order functions
#  a) Passing function as argument

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("hello")
    print(text)

hello(loud)
hello(quiet)
    
#  b) Returning function 

def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide = divisor(2)
print(divide(10))
