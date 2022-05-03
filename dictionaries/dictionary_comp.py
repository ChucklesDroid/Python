#  Dictionaries also support comprehension just like list and sets

even_no = { x:x**2 for x in range(1,11) if x%2==0 }
print(even_no)
