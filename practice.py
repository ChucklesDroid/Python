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
#  syntax for print( *objects, sep='', end='\n', file=stdout, flush=False )    #initialised with default values
from sys import stdout #for stdout
for i in range(5) :
    for j in range(5) :
        print("@", sep='', end='', file=stdout, flush=False)
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
        print(item, sep='', end=' ', file = stdout, flush=False)
    print()

#  For creating transpose of a matrix
matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
print("Matrix", matrix, sep=" ", end='\n', file=stdout, flush=False)
transpose_matrix = []
for i in range(len(matrix[0])):
    matrix_row = []
    for elmnt in matrix:
        matrix_row.append(elmnt[i])
    transpose_matrix.append(matrix_row)
print("Transpose", transpose_matrix, sep=" ", end='\n', file=stdout, flush=False)

#  Writing transpose using list comprehension
transpose = [[x[i] for x in matrix] for i in range(len(matrix[0]))]
print("Transpose", transpose, sep=' ', end='\n', file=stdout, flush=False)

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

#  update method for dictionary
#  update method not only allows to add a new key-value pair but also update an existing key-value pair
#  argument of update is usually in the form of tuples(list of tuples) or another dictionary
temp_dictionary = {14:196, 16:256}
even_no.update([(4,20)])            # Working with list of tuples as argument to update
even_no.update([(12,144)])
even_no.update(temp_dictionary)     # Working with dictionary as argument to update
print(even_no)

for x in even_no:
    print(x, end=" ")
print()

#  Strings
name = "bro Code!"
#  if not name[0].isupper():
    #  name = name.capitalize()
    #  print("Strings", name, sep=' ')
first_name = name[:3].upper()
last_name = name[4:].lower()
last_character = name[-1]
print(last_character)
#  print(first_name, last_name, sep=' ')

#  Functions 
def hello( name, last, age ):
    print("Your name is "+name+" "+last)
    print("You are"+ " "+ str(age)+ " years old")

hello( "Aakarsh", "MJ", 21 )

#  Return value
def multiply(x, y):
    return x*y
print("Mulitplication of 2 and 3 :"+ str(multiply(2,3)))

hello( age=21, name="adventerous", last="bcha" )

#  Nested function calls
#  num = input("Enter a positive whole number")
#  num = float(num)
#  num = abs(num)
#  num = round(num)
#  print(num)

#  print(round(abs(float(input("Enter a positive whole number :")))))

#  Variable argument list in Python
#  using tuples ( to be used with positional arguments )
from functools import reduce
def sum( *args ):               #creates a variable argument list of type tuple named 'args'(we can use any variable name we want)
    return reduce((lambda x,y : x+y),args)

print(sum(1,2,3,4))
#  using dictionary (to be used with keyword arguments)
def name( **kwargs ):
    for x,y in kwargs.items():
        print(y, end=" ")
name(first_name="aakarsh",second_name="Mj")
print()

##  String Format
#  animal = "cow"
#  item = "moon"
#  Regular Method
#  print("The {} jumps over the {}".format(animal, item))
#  Using positional arguments
#  print("The {1} jumps over the {0}".format(animal, item))
#  Using keyword arguments
#  print("The {animal} jumps over the {object}".format(animal="cow", object="moon"))

#  Padding while using keyword arguments with string formatting
#  left alignment
#  print("The {} jumps over the {:10}.".format("cow", "moon"))
#  print("The {} jumps over the {:<10}.".format("cow", "moon"))
#  right alignment
#  print("The {} jumps over the {:>10}.".format("cow", "moon"))
#  with middle alignment
#  print("The {animal} jumped over the {object:^10}.".format(animal="cow", object="moon"))
#  alignment along with positional argument
#  print("The {1} jumps over the {0:10}.".format(animal, item))
#  alignment with keyword argument
#  print("The {animal} jumps over the {object:10}.".format(animal="cow", object="moon"))

#  Floating point numbers with string formatting
pie=3.14159
print("The value of pie :{:.2}".format(pie))

#  Random module
import random
seq = [ x for x in range(0,11,2) ]
print(random.randint(1,2))  #Generates a random integer value inclusive of both ranges
print(random.random())        #Generates a floating point value b/w 0 and 1
print(random.choice(seq))
print(seq)
random.shuffle(seq)
print(seq)

#  File detection
path = r"/mnt/sda1/GITHUB/Python/practice.py"
#  path = r"/mnt/sda1/GITHUB/Python"
import os
if os.path.exists(path):
    print("Path is valid")
    if os.path.isfile(path):
        print("{}: is a file".format(path))
    elif os.path.isdir(path):
        print("{}: is a folder".format(path))
else:
    print("Path is invalid")

#  Reading a file
#  print("Reading a file")
#  reading entire file and returning it as string
#  file = open('demo.txt', 'rb')
#  print(file.read())

#  reading only limited characters at a time
#  print(file.read(5))

#  reading a file line by line
#  print(file.readline())

#  reading an entire file as list of lines
#  lines = file.readlines()
#  print(lines)

#  reading a file by iterating through the file object
#  for line in file:
    #  print(line, end='')
#  file.close()

#  writing to file in binary format
try:
    with open("demo.txt", 'wb+') as file:
        txt='This is {number} line\n'
        for i in range(1,5):
            file.write(txt.format(number=i).encode('utf-8'))
        file.seek(0,0)
        print(file.read().decode('utf-8'))
except Exception as e:
    print(e)
    print("Unexpected termination")

#  Copying files 
import shutil
#  shutil.copy("demo.txt", 'demo_copy.txt')
#  print(os.listdir('.'))
#  shutil.copyfile("demo.txt", 'demo_copy.txt', follow_symlinks=False)
#  shutil.copy("demo.txt", 'demo_copy.txt', follow_symlinks=True)
#  shutil.copy2("demo.txt", 'democopy.txt', follow_symlinks=True)

#  Moving a file/folder
#  os.replace('demo_copy.txt', '../demo_copy.txt')

#  Deleting a file/folder
#  os.remove() - removes a file 
#  os.rmdir() - removes an empty directory
#  shutil.rmtree() - removes a directory( regardless of it being empty or having files )

#  os.remove('demo.txt')
#  os.remove('demo_copy.txt')
#  os.remove('democopy.txt')

#  Higher order function: - function either acception functions as arguments or functions returning functions
#  1. Passing a function
def loud(text):
    return text.upper()

def silent(text):
    return text.lower()

def hello(func):
    hello = func("hello")
    print(hello)

hello(loud)
hello(silent)

#  2.Returning a function
def divisor(x):
    def dividend(y):
        return y/x
    return dividend

func = divisor(2)
print(func(3))

#  print( squares := [ x**2 for x in range(1,11) ] )


#  Multi-threading in python
import time
import threading

def counter(num):
    count = num
    while count >= 0:
        time.sleep(1)
        print(count-num+1)
        count += 1


thread1 = threading.Thread(target=counter, name="Thread1", args=(100,))
thread1.daemon = True
thread1.start()


print("Total threads:" + str(threading.active_count()))
print("Thread enumerate" + str(threading.enumerate()))

input("Do you want to continue")
print("Time taken by main thread: "+ str(time.perf_counter()))
