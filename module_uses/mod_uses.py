#  ***********************************
#  __name__ = __main__
#  ***********************************

#  use case scenarios:-
#  1. In python modules can either run as standalone programs 
#  2. or can be imported into other modules

#  Python interpreter sets "special variables", one of which is __name__
#  Python will assign __name__ the value of __main__ if its the initial module being run

import module2

print(__name__)
print(module2.__name__)  # Imported modules will have a name equal to name of module where as the module which is run directly will have a name __main__

module2.hello()


#  Alternatively we can also do this
def main():
    print("main function of the calling module")

if __name__ == "__main__":
    main()

