#  Indexing operator[] = gives access to a sequence's element ( string,tuples,lists )

name = 'aakarsh MJ' #String created

print(name)
if( name[0].islower() ):
    name = name.capitalize() #capitalizes the first letter of the word and lowercases the remaining letters

print(name)

first_name = name[:7].upper() #capitalizes the entire word
print(first_name)
last_name = name[8:].lower()  #lowercases the entire word
print(last_name)

new_name = "aakarsh mj!"
last_char = new_name[-1]
print(last_char)
