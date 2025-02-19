# ITP Week 1 Day 4 Exercise

# EASY

lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# 1. loop through the lowercase and print each element

for lowletter in lowercase :
    print(lowletter)

# 2. loop through the lowercase and print the capitalization of each element
# MEDIUM

for upletter in lowercase:
 print(upletter.upper())

# 1. create a new variable called uppercase with an empty list
uppercase = []
reversecase = []
# 2. loop through the lowercase list
    # 2a. append the capitalization of each element to the uppercase list

for letter in lowercase:
    uppercase.append(letter.upper())
print(uppercase)

for letter in lowercase:
    reversecase.insert(0,letter.upper())
print(reversecase)
# HARD

# A safe password has a minimum of (1) uppercase, (1) lowercase, (1) number, (1) special character.

#password = "MySuperSafePassword!@34"

password = input("Enter a strong password:")

special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

# 1. create the following variables and assign them Booleans as False
    # has_uppercase
    # has_lowercase
    # has_number
    # has_special_char

has_uppercase = False
has_lowercase = False
has_number = False
has_special_char = False

# 2. loop through the string password (same as a list)
# OR you can create a new list variable of the string password
# using list(string) NOTE: assign it a new variable as such:
# password_list = list(password) prior to looping.

password_list = list(password)

# 3. For each iteration of the loop, create a if statement
# check to see if it exists in any of the list by using IN
# if it does exist, update the appropriate variable and CONTINUE
# not break.

for letter in password_list:
    if letter in lowercase:
        has_lowercase = True
    elif letter in uppercase:
        has_uppercase = True  
    elif letter in special_char: 
        has_special_char = True  
    elif int(letter) in range(10):
        has_number = True   
print("Has a lowercase:", has_lowercase)
print("Has a number:", has_number) 
print("Has a lowrcase:", has_lowercase)
print("Has an uppercase:", has_uppercase)
print("Has a special character:", has_special_char)


# NOTE: to see if it has a number, use range from 0 - 10!

# 4. do a final check to see if all of your variables are TRUE
# by using the AND operator for all 4 conditions. (This is done for you, uncomment below)

final_result = has_uppercase == True and has_lowercase == True and has_number == True and has_special_char == True
if final_result == True:
    print("You have a safe password")
else:
    print("You have a weak password, please try again")

# NOTE: we can shorthand this by just checking if the variable exists (returns True)
#final_result_shorthand = has_uppercase and has_lowercase and has_number and has_special_char
# this will fail the same if any one of them is False

# If the final_result is true, print "SAFE STRONG PASSWORD"
# else, print "Update password: too weak"
# NOTE: this must be done outside of the loop


# BONUS: update the password variable to take in an user input!

# NIGHTMARE: in the final check, use another if statement to list why it isn't a strong password!


