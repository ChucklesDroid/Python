#  Dictionary is collection of key-value pairs. Dictionary is ordered(from 
#  python 3.6 onwards), changeable and does not contain any duplicates

capitals = {'US':'Washington',
            'UK':'London',
            'Germany':'Berlin',
            'South Korea':'Seoul'}
print(capitals)

#  To print value we will make use of specific key
print(capitals['US'])
#  print(capitals['France']) # This will generate error as this not defined in dictionary
#  So to overcome this we will make use of .get
print(capitals.get('France')) #This will give output 'NONE'

#  To add a new key to dictionary we will make use of update
capitals.update({'France':'Paris'})
print("Dictionary was updated :",end="")
print(capitals)

#  To change an existing value of a key we make use of update
capitals.update({'US':'Chicago'})
print("Value for Washington was updated",end="")
print(capitals)

#  To remove a particular key-value pair we will make use of pop
capitals.pop('US')
print("Value popped is US: ",end="")
print(capitals)

#  To clear a list make use of clear
capitals.clear()
print("Dictionary Cleared: ",end="")
print(capitals)
