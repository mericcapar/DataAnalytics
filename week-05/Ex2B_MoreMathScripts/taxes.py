monthly_salary = 4500
tax_rate = 0.23

taxes_withheld = monthly_salary * tax_rate

# Option 1: round() changes the value itself to 2 decimal places.
print(f"Taxes withheld: ${round(taxes_withheld, 2)}")
