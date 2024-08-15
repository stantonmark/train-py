
#Create a file named ex4_module.py and another named ex4_script.py.
 
#Code and test simple functions as follows:
 
#get_greeting that returns a greeting, e.g. G'day
 
#get_greeting_to that accepts a name and returns G'day [name]
 
#get_product that accepts two numbers and returns the product of those numbers
 
#get_first that accepts a list and returns the first element
 
#get_name that accepts a dict and returns the value assoc. with the name key
 
#get_circumference that accepts a radius and returns the circumference (2 * Pi * radius)
 
 

from day2_exercise4_module import greeting

def get_greeting_to(name):
    """Accepts a name and returns a greeting in the format 'G'day [name]'."""
    return f"G'day {name}"
your_name = input("please enter your name")

greeting = get_greeting_to(your_name)
print(greeting)


