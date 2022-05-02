#  frozenset :- frozenset is similar to sets except that they are immutable and therefore hashable. They can be used as keys for dictionary as well in other
#  sets as well. They are similar to sets in the way all the operations applicable on sets are also applicable on frozensets except set comprehension since
#  frozensets are immutable, unordered therefore unindexed and no duplicates are allowed

a = set("abracadbra")
b = set("alacazam")

c = { frozenset(a), frozenset(b), 'apples' }
basket = {'apples', 'oranges', 'apples', 'pears', 'oranges', 'banana'}
e = { frozenset(basket), frozenset(a) }
print(c)

d = c.union(e)
print(d)
e.update(d)
print(e)

print(e.difference(c))
print(e.intersection(c))

#  add(), remove() and clear() will not work with frozenlist since they attempt to change elements of the set and frozenset by default are immutable
