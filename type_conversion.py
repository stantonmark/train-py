# Type conversino happens implciityly in Python 

# falsey: numbers are zero numbers , empty collections/containers 
#NOTE: empty collections in JS are try


#numbers
print("using bool() wrapper")
print(bool(1)) # true
print(bool(0))  # false
print(bool(-0)) # false 

# Strings 
print(bool("hello")) # true
print(bool("")) # false 


# containers and list 
print(int(True))
print(int(False)) # False 
print(int(1.0)) # True
print(int(1.888)) # True

print("using float() wrapper")
print(float(1))
print(int(1))
print(str(1))

print(str(True))
print(type(str(True)))
print(type(str(123)))
print(type(str(123)))

# There exists methods for sets and dicts set() dict()




















