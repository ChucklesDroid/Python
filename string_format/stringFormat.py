#  str.format() = optional method that gives users more control while displaying
               #  outputs

animal = "cow"
item = "moon"

#  #  print("The "+ animal+ " jumped over the "+ item) #line from a popular nursey poem

#  #  Now to print the same thing we can make use of format method which makes use of 
#  #  placeholders '{}'( format fields ) just like format specifiers in 'printf' in C.

#  print("The {} jumped over the {}".format(animal,item))
#  #  Alternative way to do the same thing
#  print("The {} jumped over the {}".format("cow","moon"))

#  #  Now making use of positional arguments we can rewrite the above code as follows:- 
#  print("The {0} jumped over the {1}".format(animal,item))
#  print("The {1} jumped over the {0}".format(animal,item))

#  Now making use of Keyword arguments:-
print("The {animals} jumped over the {items}".format(animals="cow", items="moon"))
print("The {items} jumped over the {animals}".format(animals="cow", items="moon"))
#  We can even make use of keywords more than once:- 
print("The {animals} jumped over the {animals}".format(animals="cow", items="moon"))
#  we can do the same thing with positional arguments as well
print("The {1} jumped over the {1}".format(animal,item))


#  We can use more elegant of doing this by storing it inside a string
text = "The {} jumped over the {}"
print(text.format(animal,item))


#  Making use of 'f' or 'F' before the string literal
name = dict([("aakarsh","mj"), ("aayush","tiwary"), ("lenin","rathore")])
for first,last in name.items():
    print(f"{first:10} {last}")
    #  print(F"{first:10} {last}") #its the same thing as above
