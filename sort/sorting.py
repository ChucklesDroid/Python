#  List are sorted using list.sort() method whereas other iterables are sorted using sorted() method
#  sorted takes one extra argument(total = 3) than sort method which is iterable other than both arguments of sort and sorted are same.
#  one argument is key which takes in a function having one argument which returns a value. Basically an element of the iterable is passed to function
#  when data is complex and the function returns the value on which sorting is to be done

students = [("Aakarsh", "CSE", 21), ("Abhishek", "Architecture", 19), ("Arnav", "Electrical Engineering", 21), ("Aryan", "Mechanical", 20)]
students.sort(key=lambda age:age[1], reverse=True) # sorting on basis of course in reverse order
print(students)

#  Sorting on basis of age when iterable other than list is present
students = [("Aakarsh", "CSE", 21), ("Abhishek", "Architecture", 19), ("Arnav", "Electrical Engineering", 21), ("Aryan", "Mechanical", 20)]
sorted(students, key=lambda age:age[2]) # sorting the list on the basis of age
print(students)
