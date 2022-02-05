#  Python has 4 inbuilt data types which are used to store multiple items in one 
#  variable. Lists is one of them although all 4 have different properties and 
#  abilities. Other 3 are tuples, set and dicitionary. Lists are created using 
#  square brackets.

#  fruits = ["apples", "oranges", "bananas"]
#  #  To print the elements of the list
#  for x in fruits:
    #  print(x)

#  List elements are ordered, changeable and allow duplicate values
#  Also list elements are indexed
#  There are some methods that will change the order but in general order remains same

#  lis_el = ["apples", "oranges", "apples", "oranges"] #Duplicates are allowed
#  #  for x in lis_el:
    #  #  print(x)
#  lis_el[1] = "cherries"
#  print("value after change: "+lis_el[1]) #Values can be changed

#  To print the length of the list: we make use of len() command
#  fruits = ["apples", "oranges", "cherries", "bananas"]
#  print(len(fruits))

#  List items can be of any data types
#  list1 = ["apples", "oranges", "bananas"]
#  list2 = [1,2,3,4,5]
#  list3 = [True, False, True, True]

#  print("list1:")
#  for x in list1:
    #  print(x,end=" ")
#  print()
#  print("list2:")
#  for x in list2:
    #  print(x,end=" ")
#  print()
#  print("list3:")
#  for x in list3:
    #  print(x,end=" ")

#  Lists can also have different data types:
#  list4 = ["aakarsh", True, 2.5, 'c']
#  print("list4:")
#  for x in list4:
    #  print(x,end=" ")

#  From python's perspective lists are defined as objects with data type lists
#  list5 = ["list", 5, True]
#  print(type(list5))

#  It is also possible to create objects of list type by using list constructor
fruits = list(("apples", "cherries", "bananas")) # Note the double paranthesis
print(fruits) #We can also print the entire list by just using print function

#  Or we can also use for iterator for printing the values of the list
for x in fruits:
    print(x,end = " ")
