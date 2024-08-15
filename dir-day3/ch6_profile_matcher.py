def build_profile():
    age = int(input("Please enter your age in numbers: "))
    hobbies = []
    more = "y"  # Initialize 'more' to 'y' to start the loop

    while more.lower() == 'y' or more.lower() == "m":
        hobby = input("Please enter a hobby or 'n' to stop: ")
        if hobby.lower() == 'n':
            break
        hobbies.append(hobby)
        more = input("Enter 'm' for more hobbies or any other key to stop: ")

    profile = {"age": age, "hobbies": hobbies}
    return profile

# Get the user profile
user_profile = build_profile()

# Print the complete profile
print("Your profile:", user_profile)

# Extract and print specific details (optional)
print("User's age:", user_profile["age"])
print("User's hobbies:", ", ".join(user_profile["hobbies"]))


def match(profile_1, profile_2):
    match_quality = 0
    age_diff = profile_1["age"] - profile_2["age"]
    if age_diff <= 5 and age_diff >= -5:
        match_quality += 1
    for hobby in profile_1["hobbies"]:
        if hobby in profile_2["hobbies"]:#membership operator
            match_quality += 1
    return match_quality


