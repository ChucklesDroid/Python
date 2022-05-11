#  Map function is used to perform a certain function on each element of the variable. It takes in two arguments :- 1) is a function which performs a 
#  certain operation on the given element and returns the given value , 2) is iterable whose element would passed to the function succesively.

#  Map function would create an iterable of type 'map' comprising of elements returned by the function passed as first argument

no = [x for x in range(1,21)]
doubles = list(map(lambda x: x**2, no))
print(doubles)
