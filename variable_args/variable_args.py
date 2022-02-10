#  *args :-    its a parameter that will pack all arguments into a tuple
            #  useful so that a function can pack variable arguments
            #  Its similar to va_args in C
            #  name 'args' is not that important it can be named anything , its just a
            #  convention , '*' is more important
 
#  def foo( *args ):
    #  sum = 0
    #  for i in args:
        #  sum += i
    #  return sum

#  You can even have the following function
def foo( *operands ):
    sum = 0
    for i in operands:
        sum += i
    return sum

#  Since tuples are unchangeable to change them we can convert them into other type 
#  For eg:- list
def bar( *args ):
    sum = 0
    args = list(args)
    args[0] = 5
    for i in args:
        sum += i
    return sum

print(foo(1,2,4))
print(bar(1,2,4))
