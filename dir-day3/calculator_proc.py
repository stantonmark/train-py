
total = 0 

def add(num):
    global total 
    total += num
    return total

def sub(num):
    global total 
    total -= num
    return total

def mul(num):
    global total 
    total *= num
    return total

def div(num):
    global total 
    total /= num
    return total

def equals():
    global total
    return_value = total  
    total = 0 
    return return_value
    
     
    