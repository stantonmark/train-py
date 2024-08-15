#local 
# lives ad dies with function execution 

#global 


next_num = 1 # global 

#impure function depends on the global var 

def get_next_num():
    global next_num
    next_num += 1
    return next_num

print(get_next_num())


# suppose i wish to modify the var next_num

def increment_next_local_num():
    return next_num
    next_num = 2 
    next_num +=1
    return next_num
print(increment_next_local_num)



