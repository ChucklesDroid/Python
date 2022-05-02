#  sets are mutable, unordered hence unindexed and do not allow duplicate values. Elements of set need to be hashable i.e elements need to be immutable

a = set("abracadbra")
b = set("alacazam")

print(a, b, sep="\n")

a.add('babushka')
print(a)
a.remove('babushka')
print(a)
#  a.clear()
#  print(a)

basket = {'apples', 'oranges', 'apples', 'pears', 'oranges', 'banana'}
print('apples' in basket)
print('crabgrass' in basket)

print( a | b )  # a or b
print( a & b )  # a and b
print( a ^ b )  # a xnor b

#  a.update(b)
#  print( a )

#  c = a.union(b)
#  print(c)

print( a.intersection(b) )  # a & b
print( a.difference(b) )    # a - b

#  Set comprehension is similar to list comprehension
x = { x for x in 'abracadabra'}
y = { y for y in 'alakazam' }
print(x, y, sep="\n")
