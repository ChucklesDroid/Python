#  Iterating through a string using list comprehension
h_letters = [ letter for letter in 'human' ]
print(h_letters)

#  using lambda functions inside list
h_letters = list(map(lambda x:x, 'human'))
print(h_letters)

#  using if with list comprehension
even_no = [ x for x in range(10) if x%2==0 ]
print(even_no)

#  nested if with list comprehension
funky_list = [ x for x in range(100) if x%2==0 if x%5==0 ]
print(funky_list)

#  if..else with list comprehension
funky_list = [ "Even" if x%2==0 else "Odd" for x in range(10) ]
print(funky_list)

#  Transpose of a matrix
matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
import sys
transpose = [ [x[i] for x in matrix] for i in range(len(matrix[0])) ]
print("Transpose", transpose, sep=' ', end="\n", file=sys.stdout, flush=False)
