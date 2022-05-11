#  Filter function takes specific values from an iterable based on the value of function passed to it. It takes two arguments :- 1) a function which 
#  returns either True or False 2) an iterable. Filter function creates an iterable list comprising of elements from the iterable which when passed
#  as argument to it will return either True or False

no = [ x for x in range(1,21) ]
even_no = list(filter(lambda x: True if x%2==0 else False, no))
print(even_no)
