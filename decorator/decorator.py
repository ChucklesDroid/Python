#  Decorators in python are used to extend functionality of the given function. It's an extension of having ability to pass function 
#  as arguments.

def divide(a, b):
    return (a/b)

def extend(func):

    def inner(a, b):
        if b == 0:
            print("division by zero not possible !!")
            return 
        elif b>a:
            a,b = b,a
        return func(a, b)

    return inner


divide1 = extend(divide)
print(divide1(2,0))
