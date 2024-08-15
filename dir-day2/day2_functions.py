
# Functions wrap one more lines of code t be call one or zero times in the futre 
# Functions are always the same 
# how and when you use them will change and that is in the run time script 
# whatever bits will change you should keep them seperate 
# they can be very simple 
# beware of functions that are greater the 50 lines , handle a single resposibility 

def add(num1, num2):
    return num1 + num2

result = add(1,2)
print(result)
print(add(1,2))


def add_two_numbers(num1, num2):
    return num1 + num2

result = add_two_numbers(1,2)
print(result)
print(add_two_numbers(1,2))


def first_character_of_word_pure(word):
    print(word[0])
    
#first_character_of_word_pure(my_var):
    
my_var = "slan"

first_character_of_word_pure(my_var)

# Functions in python are objects too !
print(first_character_of_word_pure)

def subtract_two_numbers(num1, num2):
    return num1 - num2

subtract_two_numbers(2,1)
result = subtract_two_numbers(2,1)
print(result)




def open_account(name, balance):
    #openeing balance 
    balance += 100
    return (name, balance)

#Positional arguments in correct order 
acc1 = open_account("mark stanton offshore", 2500)
print(acc1)

#Positional arguments incorretc order 
#acc2 = open_account(3500, "mark stanton offshore")  here 3500 is not rght locatino 
#print(acc2)

# named arguments 
def  open_account2(name="customer", balance=0):
    balance += 100
    return (name, balance)

acc3 = open_account2
print(acc3)

acc4 = open_account2(balance= 3000, name="john smith")
print(acc4)


#1. no inputno output args aside 
def greet():
    print("hello")
    print("how are you")
    print("something else")   

greet()
result_greet = greet()
print(result_greet) # will see nothing or None 


# 2 no input has output 
def greet2():
    print("hello greet2" + "\n" + "How are you today")
     

greet2()
#result_greet = greet2()


# 3 input and output 
def greet2():
    print("hello greet2" + "\n" + "How are you today")
     

def greet3(name):
    return "hello greet2" + "\n" + "How are you today"
#result_greet = greet2()










