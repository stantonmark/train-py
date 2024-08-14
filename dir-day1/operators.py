
# expression involves operators and operands 

#% is the floor divisin  so 10 // 3 is how many times 3 goes into 10 

# 10 modulus 3 = 1 as it calculates the remained whne the first number is deivided into the second 
# 10 divided by 3 is 3 and 1 left over 

#  10 // 3 is ten divided by three which is three, it rounds down t teh nearest numebr 


print("ho" * 100)

# assignment 
# = assignment 
# compound assignment


my_num = 1
my_num += 1
my_num += 1
print(my_num)

my_string = "I "
my_string += "love "
my_string += "Python"
print(my_string)

# Walrus operator 
# :=
# Returns and asigns ins one go 
x = 1 
print(x)
print(y := 2)

# Increment and decrement operators do not exist in python 
# Optimisations were applied when creating python 
# 
x = x + 1 
print(x)


#Multiple assignment useful but not very python
x = 1; y = 2; z = 3
# May be rewritten like 
x,y,z = 4,5,6
print(x,y,z)
# used for saving dcistionay to props or list elements to indiidual variables 
my_dict = {"name": "alan", "age": 30}
name, age = my_dict["name"], my_dict["age"]
print(name,age)
my_nums = [1,2,3]
first,second,third = my_nums[0], my_nums[1], my_nums[2]

# assignment operator chaining 
x = 1 
y = 1
# may be rewritten as 
x = y =1 

# Comparison operators 
# is operator 
# it uses the internal operator id 

my_list = [1,2,3]
my_other_list=[1,2,3]
my_copied_list = my_list
print(my_list is my_other_list) # false becasue tow variable refernec two seperate objects but just happent o be teh same 
print(my_list is my_copied_list) # this is trie as it points to same obeject in memeory 
print(id(my_list))
print(id(my_other_list))
print(id(my_copied_list))












