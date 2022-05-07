#  Method overriding is only possible when function in the child class has the same function signature as the function in parent class.
#  by function signature both name and function arguments list are refered to here.

class A:
    def over(self):
        print("present inside class A")

class B(A):
    def over(self):
        print("function overridden by class B")

a = A()
b = B()
a.over()
b.over()

