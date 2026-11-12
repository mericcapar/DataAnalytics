import math

people = 38
seats_per_van = 15
cost_per_van = 250

#Round up
vans_needed = math.ceil(people / seats_per_van)
total_cost = vans_needed * cost_per_van
cost_per_person = total_cost / people

# Round up to the next cent so we collect enough money.
charge_per_person = math.ceil(cost_per_person * 100) / 100

print(f"You need {vans_needed} vans.")
print(f"The vans will cost ${total_cost:.2f}.")
print(f"Each person pays ${charge_per_person:.2f}.")

#a)The script charges $19.74 per person.
#b)38x19.74 = $750.12 collected.
#c)The vans cost $750.00 (3 vans x $250).
#d)There is 0.12 dollars left over because 750 / 38 = 19.7368...,
#which can't be paid in partial cents. Rounding up to $19.74
#means each person pays a tiny bit more than the exact share.