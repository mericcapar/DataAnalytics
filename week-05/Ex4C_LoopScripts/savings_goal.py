starting_balance = 2000
savings_goal = 10000
weekly_savings = 100
weeks_passed =0
halfway_point = savings_goal / 2
while starting_balance < savings_goal:
    starting_balance += weekly_savings
    weeks_passed += 1
    if starting_balance >= halfway_point:
        print(f"Almost there! My current balance is ${starting_balance}.")
    print(f"This week my balance increased to ${starting_balance}.")
    

print(f"Goal met! My current balance is ${starting_balance}.")
print(f"It took {weeks_passed} weeks to reach the savings goal.")



