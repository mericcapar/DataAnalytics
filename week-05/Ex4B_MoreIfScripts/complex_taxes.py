pay_rate = float(input("Enter your pay rate: "))
hours_worked = float(input("Enter the number of hours worked: "))
filing_status = input("Enter your filing status (single/joint): ").lower() 

# Weekly gross pay
if hours_worked > 40:
    regular_pay = 40 * pay_rate
    overtime_pay = (hours_worked - 40) * pay_rate * 1.5
    weekly_gross = regular_pay + overtime_pay
else:
    weekly_gross = hours_worked * pay_rate


annual_gross_pay = weekly_gross * 4 * 12 


if filing_status == "single":
    if annual_gross_pay < 12000:
        tax_rate = 0.05
    elif annual_gross_pay < 25000:
        tax_rate = 0.10
    elif annual_gross_pay < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20
elif filing_status == "joint":
    if annual_gross_pay < 12000:
        tax_rate = 0.00
    elif annual_gross_pay < 25000:
        tax_rate = 0.06
    elif annual_gross_pay < 75000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20
else:
    print("Filing status must be 'single' or 'joint'.")
    tax_rate = 0

# Apply the rate to the weekly gross pay
weekly_tax = weekly_gross * tax_rate
net_pay = weekly_gross - weekly_tax

print(f"You worked {hours_worked} hours this period.")
print(f"Because you earn ${pay_rate:.2f} per hour, "
      f"your gross weekly pay is ${weekly_gross:.2f}")
print(f"Your filing status is {filing_status}")
print(f"Your tax withholding for the week is ${weekly_tax:.2f}")
print(f"Your net pay is ${net_pay:.2f}")