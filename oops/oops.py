from car import Car

car1 = Car("maruti", "800", 2008, "white")
car2 = Car("Lamborghini", "Aventador", 2022, "blue")
#  car1.drive()
#  car1.stop()
print(car1.wheels)
print(car2.wheels)
car1.wheels = 3             #This here creates an instance variable for car1
print(car1.wheels)
print(car2.wheels)
Car.wheels = 2          
print(car1.wheels)          #It refers its instance variable which in this case has value 3
print(car2.wheels)

