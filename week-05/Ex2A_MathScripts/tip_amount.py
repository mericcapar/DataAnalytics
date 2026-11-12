# Lab 3: values come from the user with input().
bill = float(input("How much was your restaurant bill? $"))
tip_percent = float(input("What tip percentage do you want to leave? "))

tip = bill * tip_percent / 100

#output written as an f-string.
print(f"The tip on a ${bill:.2f} restaurant bill is ${tip:.2f}")

# Pitfalls with input():
# 1. input() always returns a string, so the value must be converted
#    with float() or int() before doing math with it.
# 2. If the user types something that is not a number, like "abc" or
#    "$50", float() raises a ValueError and the program crashes.
# 3. The user may type the tip as 0.20 instead of 20, which would give
#    a much smaller tip than expected.

