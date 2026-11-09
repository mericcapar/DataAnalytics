"""
Meric Capar
"""

import keyword

customer_id = 12345  # Int, because it is an ID.
customer_name = "Deodat Sharma"  # First and last name could be separate.
# String. It could be limited to set options, but that is not a must.
customer_gender = "Male"
# String in YYYY-MM-DD format. A date type could also be used.
customer_birthdate = "1980-01-01"
customer_driver_license = "D1234567"  # String, because it has letters.
customer_policy_number = "P9876543"  # String, because it has letters.

my_name = "Meric Capar"  # My full name, string.
city = "Antalya"  # The city I grew up in, string.
country = "Turkey"  # Turkey has no states, so I used the country.

print(keyword.kwlist)

# Reserved words:['False', 'None', 'True', 'and', 'as', 'assert', 
# 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 
# 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 
# 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 
# 'return', 'try', 'while', 'with', 'yield']

# if: Runs a block of code only when a condition is True.
# else: Runs a block of code when the if condition is False.
# except: Handles ^^exceptions^^ (errors) that happen while the program runs.
# break: Exits a loop early.
# def: Defines a function.