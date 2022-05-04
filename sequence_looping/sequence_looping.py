#  items allows us to access both key-value pairs of a dictionary simultaneously
dictionary = dict( [('jack','sparrow'), ('Robin','Williams'), ('Edward','Snowden')] )
print(dictionary, type(dictionary))

#  enumerate allows us to access both index as well as value of sequence
list_val = [1, 2, 3, 4, 5]
for i,v in enumerate(list_val):
    print(i, v, sep=',', end=' ')
print()

#  zip allows us to access 2 different sequences at the same time but will work as long as one of sequences exhaust or both of them exhausts
for x,y in zip(list_val, dictionary):
    print(x, dictionary[y])

#  sorted allows us to create a sorted list
for x in sorted(dictionary):
    print(x, end=' ')
print()

#  reversed allows us to access a list in reverse order
for x in reversed(dictionary):
    print(x, end=' ')
print()

#  set-sorted combination for a sequence
ls = [ 'jack', 'batman', 'superman', 'flash', 'jack', 'robin' ]
for x in sorted(set(ls)):
    print(x, end=' ')
