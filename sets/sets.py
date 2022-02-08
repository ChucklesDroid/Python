#  Sets :- is a collection of items that are unordered(hence unindexed), unchangeable
#  and do not contain duplicate values.

#  A set is faster than list

utensils = {"fork", "knife", "spoon"}       #Creation of sets
dishes = {"bowl", "plate", "cup", "knife"}

print(dishes)
print(utensils)         #On running the program multiple times it gives out different
                        #output each single time i.e the order in which elements are 
                        #displayed is different each single time
#  To add argument to the given set
#  utensils.add("spatula") 
#  print(utensils)

#  To remove element from the given set
#  utensils.remove("fork")
#  print(utensils)

#  To join two sets together and to save it one of the 2 sets use "update" command
#  utensils.update(dishes)
#  print(utensils)

#  #  To store sum of two sets in third set use 'union' command
#  dinner_table = utensils.union(dishes)
#  #  alternative could be : dinner_table = dishes.union(utensils)
#  print(dinner_table)

#  To find difference b/w two sets use 'difference' 
print(dishes.difference(utensils)) #Compares elements in dishes against utensils

#  To find common elements b/w two sets use intersection
print(dishes.intersection(utensils))
