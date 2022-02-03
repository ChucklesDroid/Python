#  Two operations can be used in string slicing :-
#  Slice constructor 
#  Extended Indexing Operation
#       Syntax :- [start:end:step] = start is inclusive , end is exclusive

name = "aakarsh mj"

#  Using Extended Index Slicing 
first_name = name[0:7]
#  shorthand would be:- name[:7]
print("First Name: "+first_name)

last_name = name[8:10]
#  shorthand would be:- name[8:]
print("Last Name: " + last_name)

#  Using step in Extended indexing
funky_name = name[0:10:2]
#  shorthand would be:- name[::2]
print(funky_name)

#  Reversing a string using a negative step 
reverse_name = name[::-1]  
print("Name reversed: "+reverse_name)


#  Using slice constructor and creating an object of type slice for indexing purposes
#  Working of slice constructor is similar to extended indexing
#  In slice constructor instead of ':' we make use of ','
website1 = "https://google.com"
website2 = "https://wikipedia.com"
slic = slice(8,-4,1)
print("Website name: " + website1[slic])
print("Website name: " + website2[slic])

