#  Loop control statements : Changes a loop's execution from its normal behaviour

#  break :- used to terminate the loop entirely
#  continue :- used to skip to the next iteration of the loop
#  pass :- does nothing, acts as a place holder

#  To take input from the user :-
#  while True:
    #  name = input("Enter your name :- ")
    #  if name != "":
        #  break 
#  print("Name entered: "+name)

#  To display user's phone no without 'dashes'
#  phone_number = "123-456-7890"
#  for i in phone_number:
    #  if i == '-':
        #  continue
    #  print(i,end='')

#  To print numbers 1 to 20 but not print 13
for i in range(1,21): #since end is exclusive in range syntax
    if i == 13:
        pass
    else:
        print(i)
    
    
