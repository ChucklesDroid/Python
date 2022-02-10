#  positional args :-  order of arguments matter 
#  keyword args :- arguments preceded by an identifier( which are names of variables
#  in the argument list) when we pass them to function order of arguments do not 
#  matter,unlike positional arguments python knows the name of arguments which 
#  it recievers

def hello( first_name, middle_name, last_name ):
    print("Hello " + first_name+ " "+ middle_name+ " "+ last_name)

hello( "aakarsh", "m", "j" )    #positional arguments
hello( middle_name="m", last_name="j", first_name="aakarsh" ) #keyword arguments 

