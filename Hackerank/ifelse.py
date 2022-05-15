n = int(input().strip()) 
# input() function returns a string while strip() function removes leading and trailing spaces(
# since in this case it does not have any argument)

if n%2!=0:
    print("Weird")
else:
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")
