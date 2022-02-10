#  Similar to printf we can use format specification in print 

#  To limit fractional points to be printed
pi = 3.14159        #This would approximate the value to be printed
print("Value of pi :- {:.2f}".format(pi))   #Note:- This would round of the value

#  To include ',' for every thousand's place
number = 10000
print("The number printed : {:,}".format(number))

#  To print the number in binary form
print("The binary representation is: {:b}".format(number))

#  To print the number in octal form 
print("The octal representation is: {:o}".format(number))

#  To print the hexadecimal form(or X)
print("The hexadecimal representation is: {:x}".format(number))

#  To print the scientific form(or E)
print("The scientific representation is: {:e}".format(number))



