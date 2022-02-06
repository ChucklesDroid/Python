fruits = list(("apples", "bananas", "cherries")) 
#using constructor to intialise list elements
print(fruits)

# To append to list
fruits.append("melons") #appends to the end of list
print(fruits)

# To remove a particular element from list
fruits.remove("bananas")
print(fruits)

#  To pop element from list
fruits.pop() #popping removes the last element from the list
print(fruits)

#  To insert an element at a particular position 
fruits.insert(1,"melons") #inserts melons at index 1
print(fruits)

#  To sort a given list
fruits.sort()
print(fruits)

#  To clear the list
fruits.clear() #Clears the list
print(fruits)
