#  To print anything to the screen 
print("Helloworld")

#  variables
#  string data type
first_name = "Aakarsh"
last_name = "MJ"
print(first_name)
print("Hello " + first_name)
print("hello " + first_name + " " + last_name)

#  To print data type of a given variable
print(type(first_name))
#  NOTE:- No arithmetic operations can be performed on strings

age = 21
age += 1 
#  To print variables along with string we make use of typecasting
print("Your age is " + str(age) )
print(type(age)) 

#  Float variables
turtle_age = 250.5 
print(turtle_age)
print(type(turtle_age))

#  Boolean variables
human = True
print(human)
print(type(human))

#  With type casting
print("Are you human :" + str(human))

#  Alternate way to declare variables
#  first_name,last_name,age,human = "Aakarsh","MJ",21,True
#  Multiple assignments
Patrick = Spongebob = Sandy = Squidward = 30
print("Spongebob = "+ str(Spongebob)+ ",Squidward = "+str(Squidward) + ", Sandy = " + str(Sandy) + ",Patrick = " + str(Patrick))
print()

#  String Operations
name = "Bro Code"
print(len(name))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.find("o"))
print(name.count("o"))
print(name.isdigit())
print(name.isalpha())
print(name.replace("o","a"))
print(name*3)                   # To print name 3 times

#  String Concatenation
x = 3
y = 1.25
z = "3"
print("Value of x is :" + str(x))       #String Concatenation
print("Value of y is :" + str(y))
print(z*3)                              #Shorthand method to print z 3 times
print(int(z)*3)                         #Shorthand method to print int(z)*3


#  Accepting user input 
#  age = int(input("Enter your age :"))
#  name = input("Enter your name :")
#  height = float(input("Enter your height :"))

#  print("Your name is :" + name)
#  print("Your age is :" + str(age))
#  print("Your height is :" + str(height))

#  Math Function
import math
pi = 3.14
x , y , z = 1, 2, 3
print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(pow(pi,2))
print(math.sqrt(pi))
print(max(x, y, z))
print(min(x, y, z))

#  String slicing in Python 
#  1. using indexing operator with strings
name = "Aakarsh MJ"
first_name = name[:7]
last_name = name[8:]
funky_name = name[::2]
print(first_name)
print(last_name)
print(funky_name)
#  Reversing a string
reverse = name[::-1]
print(reverse)
#  2. using slice function
#  slice function creates a slice object
first_name_slice = slice(0,7)
#  using slice function to extract name of websites from url
website1 = "https://google.com"
website2 = "https://facebook.com"
website_slice = slice(8,-4)
print(name[first_name_slice])
print(website1[website_slice])
print(website2[website_slice])
#  3. Slice operator is also used to copy a list
list1 = [1,2,3]
list2 = list1   # This creates a reference variable list2 which points to list1 basically they are pointing to same object
list3 = list1[:]# This creates a copy of the list list1 and saves in list variable list3 i.e they are pointing to different objects

#  if statements in Python
#  age = int(input("Enter your age :"))
#  if age == 100:
    #  print("You are century old")
#  elif age >= 18:
    #  print("You are an adult")
#  elif age < 0:
    #  print("You are not born yet!!")
#  else:
    #  print("You are a kid")

#  Infinite while loops
#  while 1:
    #  print("testing infinite loop")

#  while loop
#  name = ""
#  while not len(name) :
    #  name = input("Enter your name :")
#  2nd Alternative method using None object of class NoneType
#  name = None
#  while not name :
    #  name = input("Enter your name :")

#  Using time to make the current thread sleep for 1s
#  import time
#  for count in range(10,0,-1) :
    #  print(count)
    #  time.sleep(1)
#  print("Happy New Year !!")

#  Nested loop
#  syntax for print( *objects, sep='', end='\n', file=sys.stdout, flush=False )    #initialised with default values
import sys  #for sys.stdout
for i in range(5) :
    for j in range(5) :
        print("@", sep='', end='', file=sys.stdout, flush=False)
    print()

#  Loop control statements
#  pass = acts as a placeholder does nothing
#  break = exits out of the current loop
#  continue = skips the current iteration and executes the next

#  using multiple arguments in print function in python
name = "Aakarsh"
print("My name is",name)    # On using multiple arguments in print function then by default sep is initialised as sep=' '

#  Fibonnaci Series
a,b = 0,1
while a<100 :
    print(a,end=',')
    a,b = b,a+b
print()                     # To improve formatting of text

#  Lists and 2d Lists
games = ["football", 'cricket', 'table-tennis', 'snooker']
#  lists are immutable
games[1] = "pagal-panti"
#  print(games)
#  using indexing operator to clear a list
#  (1)to clear part of a list
games[1:2] = []             # It clears element at 1st position from the list
print(games)
#  (2)to clear entire list
games[:] = []
print(games)

#  2d lists
beverages = ['coke', 'mojito', 'gin']
dessert = ['white traufel pastry', 'rassugula']
full_course = ['thali', 'kimchi-rice', 'ramen']
food=[full_course, beverages, dessert]
for course in food:
    for item in course:
        print(item, sep='', end=' ', file = sys.stdout, flush=False)
    print()

#  For creating transpose of a matrix
matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
print("Matrix", matrix, sep=" ", end='\n', file=sys.stdout, flush=False)
transpose_matrix = []
for i in range(len(matrix[0])):
    matrix_row = []
    for elmnt in matrix:
        matrix_row.append(elmnt[i])
    transpose_matrix.append(matrix_row)
print("Transpose", transpose_matrix, sep=" ", end='\n', file=sys.stdout, flush=False)

#  Writing transpose using list comprehension
transpose = [[x[i] for x in matrix] for i in range(len(matrix[0]))]
print("Transpose", transpose, sep=' ', end='\n', file=sys.stdout, flush=False)

#  Dictionary built in data structure
#  dictionary are collection of key-value pairs. Dictionary are ordered, mutable but no duplicate keys should be present in a given dictionary
people = { 'sasha':4198, 'grey':4076, 'sam':4329 }
people1 = dict({'lockhart':4290, 'dieingbird':4300, 'Tolstoy':6790})
people2 = dict([('Bordeaux',4500), ('Paris',2300), ('Berlin',4500)])
people3 = dict( Bordeaux=4500, Paris=2300, Berlin=4500 )

print(people, people1, people2, people3, sep='\n')
print(people.get('ronan'))  # Safer way to access values in a dictionary

#  Adding values in a dictionary
people['ronan'] = 4309
people['groot'] = 5390

#  Use of membership operator
print( 'ronan' in people )
print( 'sasha' not in people )

#  Dictionary comprehension
even_no = { x:x**2 for x in range(1,11) if x%2==0 }
print(even_no, type(even_no))
