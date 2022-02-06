#  To create tuple with one element
fruits = ("apples",)
print(type(fruits))

beverages = ("beer") #creates a string
print(type(beverages))

#  Tupple can also be created using tuple constructor
nationalities = tuple(("indian", "germany", "canada", "US", "UK"))
print(type(nationalities))

#  We can access tuple elements by referencing 
print("nationalities[1] = "+nationalities[1])

#  Negative indexing means start from the end 
print("nationalities[4] = nationalites[-1] = "+ nationalities[-1])

#  For printing elements in a given range
for i in range (2,5):
    print(nationalities[i],end=' ')
print()
#  Alternative way :-
print(nationalities[2:5])
