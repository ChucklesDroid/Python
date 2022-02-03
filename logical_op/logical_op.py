#  Logical Operators 
#  and,or and not are the logical operators used in python
temp = int(input("What is the temperature today ?"))

#  if temp<0 or temp>30:
    #  print("Extreme Temperature detected !")
    #  print("Stay indoors")
#  elif temp>0 and temp<18:
    #  print("Nice weather")
#  else:
    #  print("A nice weather is predicted today")
    #  print("You should explore outside")

#  We would not making use of not operator
if not(temp<0 or temp>30):
    print("Extreme Temperature detected !")
    print("Stay indoors")
else:
    print("A nice weather is predicted today")
    print("You should explore outside")
