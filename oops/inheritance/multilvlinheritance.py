#  Multi Level Inheritance
#  here C inherits from B and B inherits from A

class A:
    def A(self):
        print("Parent class of B")

class B(A):
    def B(self):
        print("Child class of A")

class C(B):
    def C(self):
        print("Child class of B")

a = A()
b = B()
c = C()

c.C()
c.A()
c.B()
