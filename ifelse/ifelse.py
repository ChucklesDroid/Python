#  if else statements in python 
#  python makes use of indentation to define ifelse(whitespaces) blocks we need to make
#  sure that if we are not passing anything in the block to make use of 'pass' 


age = int(input("what is your age ? "))

if age == 100:
    print("You are ancient")
elif age >= 18 and age <= 25:
    print("you are an adult but have no responsibilities")
elif age > 25:
    print("Real life sucks for you ")
elif age > 12 and age < 18:
    print("You are a carefree teenager")
else:
    print("You are a cry baby")

