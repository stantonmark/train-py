
# Create a script 
# prompt the user to input hi/her birth year and capture itin variable named birth year 
# convert birth_name in to an int 
#4. If the user was born between 1946 and 1965, print Baby Boomer to the console.
#5. If the user was born between 1966 and 1976, print Generation X to the console.
#6. If the user was born between 1977 and 1994, print Millennial to the console.
#7. If the user was born in 1995 or beyond, print Generation Z to the console


birth_year = int(input("please enter your birth year: "))
if birth_year >= 1946 and birth_year <= 1965:
    print("Baby Boomer")
    
if birth_year >= 1966 and birth_year <= 1976:
    print("Generation X")

if birth_year >= 1977 and birth_year <= 1994:
    print("Millennial")
1979
if birth_year >= 1995:
    print("Generation Z")

