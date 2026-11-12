# Rule of 72: years to double = 72 / interest rate (as a whole number).
savings = 5000
interest_rate = 6  

years_to_double = 72 / interest_rate
doubled_savings = savings * 2

print("Your current savings is " + format(savings, ".2f") + ".")

print("At a " + format(interest_rate / 100, ".0%")
      + " interest rate, your savings account will be")

print("worth " + format(doubled_savings, ".2f") + " in "
      + format(years_to_double, ".1f") + " years")