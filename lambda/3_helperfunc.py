#  filter - It takes 2 arguments:- function and iterable, it returns an iterable consisting of elements which return true value for the given passed function
#  map :- it also takes 2 arguments:- function and iterable, it applies the function on each element of the iterable and returns an object of type map consisting of elements which are returned by the function
#  reduce :- it performs a rolling computation as specified by the passed function to the neighbouring elements, by taking a function and an iterable as arguments and returns the final computed value.

#  Example of filter
numbers = list(range(1,10))
even_numbers = list(filter((lambda x: True if x%2==0 else False), numbers))
print(even_numbers)

#  Example of map
square_root = list(map((lambda x: x**2), even_numbers))
print(square_root)

#  Example of reduce
#  1st example:- To calculate sum of first 9 numbers
from functools import reduce
sum = reduce((lambda x,y: x+y), numbers)
print(sum)

#  2nd example:- To calculate greatest of given numbers in a list
import sys
greatest = reduce( (lambda x,y: x if x>=y else y), numbers )
print("Greatest :",greatest, sep=" ", end="\n", file=sys.stdout, flush=False)
