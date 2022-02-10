#  Using print in a similar fashion as printf in C
name = 'Aakarsh'
print("Hello {}. Nice to meet you".format(name))

#  To add padding to format field make use of colons inside it
#  By default the padding is left aligned

print("Hello {:10}. Nice to meet you".format(name))

#  To make the padding left aligned we can make use of '<' before the number while 
#  padding

print("Hello {:<10}. Nice to meet you".format(name))

#  To make the padding right aligned we can make use of '>' before the number
print("Hello {:>10}. Nice to meet you".format(name))

#  We can even make the padding to be centre aligned by making use of '^'
print("Hello {:^10}. Nice to meet you".format(name))


#  we can even make use of padding with positional and keyword arguments
#  positional argument
print("Hello {1:>10}. Nice to meet you".format(name,"happy","aakash"))

#  keyword arguments
print("Hello {name2:>10}. Nice to meet you".format(names="aakarsh", name1="happy", name2="aakash"))



