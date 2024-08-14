##2. Declare and assign one variable for each of the items of data tabled below.
 
#Description             Value
##ID                      1234
#First name              John
#Last name               Doe
#Checked bags            False
#Flight                  LGW to CDG
#Flight time             1 hour 15 minutes
##Visited countries       Latvia, Guyana, Yemen, Uzbekistan
 
#3. Print each variable and its data type to the console.



ID = int(1234)
print(type(ID))
print(ID)

print("printing first name and its class")
first_name = str('John')
last_name = str('Doe')
print(type(first_name))
print(f"fullname is: {first_name} {last_name}")


checked_bags = bool(False)
print(type(checked_bags))
print(f"your checked in bags is: {checked_bags}")

flight_time = float(1.5)
print(type(flight_time))
print(f"flight time from LGW to CDG is: {flight_time}  hours")


Visited_countries=["Latvia", "Guyana", "Yemen", "Uzbekistan"]
Visited_countries_set=("Latvia", "Guyana", "Yemen", "Uzbekistan")
print(type(Visited_countries))
print(f"you visited {Visited_countries}")








