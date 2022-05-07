#  method chaining:- involves calling multiple methods sequentially which performs an action on the same object and returns self

class Car():
    def engine_start(self):
        print("Start the car engine")
        return self

    def drive(self):
        print("Drive the car")
        return self

    def brake(self):
        print("Step on the brakes")
        return self

    def engine_stop(self):
        print("Stop the car engine")
        return self


car = Car()
#  car.engine_start().drive().brake().engine_stop()
#  The above code is not readable to make it readable we can make use of backspace or paranthesis
#  1. using backspace
car.engine_start()\
    .drive()\
    .brake()\
    .engine_stop()

#  2.using paranthesis (while using panda library for example)
#  refer the link below to view the example:-
#  https://note.nkmk.me/en/python-method-chain-line-break/


