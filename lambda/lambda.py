#  Lambda function usage
numbers = [1,2,3,4,5]
squared_numbers = []
square = lambda n: n*n      #creating lambda functions
for n in numbers:
    squared_numbers.append(square(n))
print("Squared numbers :", squared_numbers, sep=' ', end='\n', file=sys.stdout, flush=False)

