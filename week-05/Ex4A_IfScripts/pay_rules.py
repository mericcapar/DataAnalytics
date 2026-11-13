pay_rate = float(input("Enter your pay rate: "))
hours_worked = float(input("Enter the number of hours worked: "))

if hours_worked <= 40:
    gross_pay = pay_rate * hours_worked
    print(f"Your gross pay is ${gross_pay:.2f}")
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = (pay_rate * 40) + overtime_pay
    print(f"Your gross pay is ${gross_pay:.2f}")
