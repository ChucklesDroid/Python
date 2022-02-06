#  Tuples are immutable and cannot be changed once created 
#  Although there is a workaround that can be used instead
#  Convert tuple into list, make the required changes and then convert it back into tuple

fruits = ("apples", "bananas", "mangoes")
fastfood = ("burgers", "pizza", "spaghetti")
conv_list = list(fruits)
conv_list.append("cherries")
fruits = tuple(conv_list)
print(fruits)

#  To create tupple by combining multiple tuples
food = fruits + fastfood
print(food)
