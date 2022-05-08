#  Abstract class:- 1) It prevents a user from creating an object of the class.
                 #  2) It compels the user to override the methods present in the abstract class

#  abstract class:- a class which contains one or more abstract methods.
#  abstract method:- a method that has a declaration but no implementation.

#  ---------------------------------------------
#  Syntax for abstract class in python
#  abc stands for abstract base class
from abc import ABC, abstractmethod

class base(ABC):
    @abstractmethod
    def go(self):
        pass

#  ---------------------------------------------

class derived(base):
    def go(self):
        print("Derived Class")

#  b = base() #This will produce error since abstract class cannot have objects
d = derived()
d.go()
