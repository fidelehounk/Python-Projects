# ITP Week 1 Day 2 (In-Class) Practice

# a. assign a variable 'subtotal' to 17.75

subtotal = 175.75
print("The value of subtotal is", subtotal)

# b. assign a variable 'tax_percentage' to .18

tax_percentage = 0.18
print("The tax percentage is", tax_percentage)

# c. assign a variable 'tax_amount' to the product of subtotal and tax_percentage  

tax_amount = round(subtotal*tax_percentage)
print("The tax amount is", round(tax_amount, 2))

# d. assign a variable 'total' to the sum of subtotal and tax_amount

total = subtotal + tax_amount
print("The Total is", round(total, 2))