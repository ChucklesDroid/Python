#  print statement has a parameter 'end' which by default has value '\n'
#  but we can also explicity provide it value according to our needs

#  Example program to print pattern

x = int( input("Enter rows: ") )
y = int( input("Enter columns: ") )
for rows in range(x):
    for columns in range(y):
        print("@",end='')
    print()         #By default prints newline character 
