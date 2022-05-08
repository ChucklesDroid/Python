#  Super has 2 use cases in python :-
#  1). To access parent methods in a single inheritance
#  2). In cooperative multiple inheritance

class base:
    def __init__(self):
        print("__Base__init__")
        
class Child1(base):
    def __init__(self):
        super().__init__()
        print("__Child1__init__")

class Child2(base):
    def __init__(self):
        super().__init__()
        print("__Child2__init__")

class Child3( Child1, Child2 ):
    def __init__(self):
        super().__init__()
        print("__Child3__init__")

c4 = Child3()
