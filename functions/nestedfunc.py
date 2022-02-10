#  Nested Function calls :-    function calls inside other function calls
                            #  innermost function calls are resolved first 
                            #  returned value is used as an argument for the next 
                            #  outter function

#  num = input("Enter a positive whole number :")
#  num = float(num)    #Since the value entered would be stored as string
#  num = abs(num)      #Since the value entered can be negative therefore magnitude is 
                    #  #taken      
#  num = round(num)    #Value is rounded off since the initial requirement was a positive
                    #  #whole number
#  print(num)


#  We will make use of nested function calls to recreate the above code using lesslines

print(round(abs(float(input("Enter a positive whole no: ")))))
