# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00
# Calculate the unknown

total_due = food_cost + tax + tip

# Display the results
#print("The total due is " + str(total_due))

#Because the total_due is a float, we need to format it to string so we can concatenate it with the rest of the string.
#Instead of using this we could use f-strings. 

print("Food cost is " + str(food_cost) + " and the tax is " + str(tax))
#print("Tip is " + str(tip))
print("Tip is " + format(tip, ".2f"))
print("Total cost is " + str(total_due))