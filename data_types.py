
my_list = ["bat", "ball", "gloves"]
print(type(my_list))
print(my_list[0])
print(len(my_list))
my_list.append("shoes")
print(my_list)
my_list[0] = 'stumps'


#Tuple 
my_tuple = ("bat", "ball", "gloves")
#my_tuple[0] = 'stumps'  # you cant change a tuple 

my_utlimate_tuple = (42, "The ulimate answer")
print(my_utlimate_tuple)

#my_other_tuple = tuple(1, "the ultipmate answer")

# Much easier to use square brackets instead of tuple 


# Sets 
#no duplicates in sets, not ordered
# does not keep order 

my_set = {1,2,3,4,5,7,7,7}
print(my_set)
my_other_set = {'one', 'two', 'three', 'four', 'five','a-1'}
print(my_other_set)
print(type(my_other_set))

    
########

# Dict 
# dictionary 
# values: key: value pairs 
# keys may be of any type but are ysually strngs 
# Keys must be unique 
# values may be of any type and may be duplicated 
# NOTE Dict is not the same as an object even though both use curly braces and key : value pairs 
# Objetcs are made by clases 
# Theoretically everything is  an objetc in python 

my_dict = {"name": "fred", "age": "42"}
print(my_dict)



# None type (equicilant to null in other languages)

my_none = None
print(my_none)
print(type(my_none))