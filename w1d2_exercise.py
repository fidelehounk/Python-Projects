# ITP Week 1 Day 2 Exercise

# We will replicate a number magic trick with Python! Below is the magic trick that we will convert! Below that is the python instructions, you will need to complete.

# Step 1: Pick a number from 1 - 9
# Step 2: Multiple by 2
# Step 3: Add 10 to the total
# Step 4: Divide by 2
# Step 5: Subtract by the original number
# Final Number: 5

# assign a variable "step_1" to a number of your choice between 1 - 9
step_1 = 8
print("Step 1 : ", step_1)

#Bonus 
# step_1 = int(input("your number "))
# print("Step_=1 :",  step_1)

# assign a variable "step_2" to the product of step_1 and the number 2

step_2 = step_1 * 2
print("Step 2 :", step_2)

# assign a variable "step_3" to the sum of step_2 and the number 10

step_3 = step_2 + 10
print("Step 3 :", step_3)


# assign a variable "step_4" to the quotient of step_3 and the number 2

step_4 = int(step_3 / 2)
print("Step 4 :", step_4)

# assign a variable "step_5" to the difference between step_4 and step_1

step_5 = step_4 - step_1
print("Step 5 :", step_5)

# print step_5 and you should see 5!

print(step_5)


# BONUS 1: can you convert step_1 to prompt a user's input?
    # HINT: you need to cast step_1 to a int because user input is a type string.

#step_1 = int(input("your number "))
step_1 = input ("Input your number: ")
yournumber = int (step_1)
yournumber *= 2
yournumber += 10
yournumber /= 2
yournumber -= int(step_1)
print("Your number is: ", int(yournumber))

# BONUS 2: can you REFACTOR using less variables?
