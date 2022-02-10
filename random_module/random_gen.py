#  we will be making use of random module 
import random

#  To generate a random integer in the given range
x = random.randint(1,5)
print("Random integer in the range 1-5: {}".format(x))  #Takes 2 mandatory arguments

#  To generate a random float value 
y = random.random()     #Will generate a random no b/w 0-1(random.random() does not take any argument)
print("Random float value in the range 0-1: {}".format(y))


#  To choose random element from a list(list is a type of array in python)
stonepprscsr = ["rock", "paper", "scissor"]
z = random.choice(stonepprscsr)
print("Random stone paper scissor choice: {}".format(z))

#  To shuffle elements of a list
cards = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A' ]
random.shuffle(cards)
print(cards)
