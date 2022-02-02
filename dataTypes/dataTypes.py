#  String Data Types
#  To create variable we dont have to specify variable type 
#  We cannot perform maths on strings
name = "Bro"
print("hello "+name )

#  String Concatenation
#  To print the type of variable use 'type' function
print(type(name))

#  We can combine two variables as long as they are of similar type
last_name = "bro"
first_name = "code"
full_name = first_name + last_name
print("hello "+full_name)

#  Integer Data types
#  Lets try printing combination of string and integer values
age = 21
#  print("Your age is:" + age)     #faces error as discussed earlier
#  To resolve the issue we make use of typecasting
#  to cast integer to string we use str funcion
print("Your age is: "+str(age))

#  Float data Types
height = 185.5
print("My height is :" + str(height) +"cms")

#  Boolean Data Types
#  To print boolean values we will make use of initializers 'True' and 'False' 
humanCode = True 
print("Are you human ? " + str(humanCode))
