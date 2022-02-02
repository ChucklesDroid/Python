#  By default input takes value as string so if we want a specific type we have to cast
#  the input to that type,Example:-
#  Note:-Again no mathematical operation will be performed on strings in python

name = input("What is your name ? ")    #Takes normal string as input 
#  age = input("Enter your age")           #Takes age input as string
print(name)
#  print(type(age))

#  If we have to take input of different type then following methods can be used
age = int(input("what is your age ? "))
print(age)
#  print(type(age))

#  If we have to take float value as input 
height = float(input("what is your height ? "))
print(height)
