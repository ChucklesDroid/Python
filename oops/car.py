class Car:
    wheels = 4                  #class variable
    def __init__(self, make, model, year, color):
        self.make = make        #Instance variable
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("{make} is driving".format(make=self.make))
    def stop(self):
        print("{make} is stopped.".format(make=self.make))
