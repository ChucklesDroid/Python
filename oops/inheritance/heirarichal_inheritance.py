#  Inheritance

class Animals:
    alive = True

    def breathe(self, type):
        print("{animal} is breathing".format(animal=type))

    def sleep(self, type):
        print("{animal} is sleeping".format(animal=type))

class Rabbit(Animals):
    def hop(self, name):
        print("{} is hopping".format(name))

class Fish(Animals):
    def swim(self, name):
        print("{} is swimming".format(name))

class Hawk(Animals):
    def fly(self, name):
        print("{} is flying".format(name))

rabbit = Rabbit()
rabbit.breathe("rabbit")
rabbit.hop("bunny")

fish = Fish()
fish.breathe("fish")
fish.swim("percy")

hawk = Hawk()
hawk.breathe("hawk")
hawk.fly("robert")
