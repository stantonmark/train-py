

#args are multiple positional arguments , multiple packed into a tuple 
# kwargs - multiple named keyword 
# must be after args 

def greet(name, hobbies):
    print(f"hello my name is {name} and my hobbies are {hobbies}")
    
    
greet("Art", "golf, music, basketball")
greet("Art", ["golf", "music", "basketball"])


def greet_with_args(name, *hobbies):
    print(f"Hello my name is {name}")
    print(f"my hobbies are {hobbies}")
    print("my non formatted hobbies are" + str(hobbies))

greet_with_args("Billy")
greet_with_args("Billy", "golf", "music", "basketball")


# kwargs (keyword arguments)
# Zero, one or many named arguments get packed into the dict 

def greet_with_kwargs(name, *hobbies, **other_details):
    print(f"hello my name is {name}")
    print(f"my hobbies aer {hobbies}")
    print(f"i also have other details {other_details}")
    
    
greet_with_kwargs("billy no mates")
greet_with_kwargs("Mark", "muisc", "golf", county="mayo", country="Ireland")








                  
    

