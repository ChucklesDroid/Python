#  We can pass objects as argument to function. Also python supports duck typing. In short it can be summarised as " if it walks like a duck, talks like a 
#  duck. it must be a duck". It is a concept where class is considered less important than its methods/attributes. Class type is not checked if minimum
#  methods/attributes are present

class duck:
    def walk(self):
        print("The duck is walking")
    
    def talk(self):
        print("The duck is quaking")

class chicken:
    def walk(self):
        print("The chicken is walking")

    def talk(self):
        print("The chicken is chirping")


class Person:
    def hello(self, duck):
        duck.walk()
        duck.talk()

ducko = duck()
chick = chicken()
person = Person()
person.hello(chick)
person.hello(ducko)
