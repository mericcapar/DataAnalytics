# name = input("Enter your name: ")
# salary = float(input("Enter your salary: "))

# if salary > 5000:
#     print(f"{name}, you are eligible for a bonus.")
# print('Done!')

# name = input("Enter your employee name: ")
# number = int(input("Enter your performance score: "))

# print(f"Employee Name: {name}")
# print(f"Performance Score: {number}")
# if number >=80:
#     print("Excellent Performance!")
# else:
#     print("Needs improvement.")

name = input("Enter your employee name: ")
number = int(input("Enter your performance score: "))
rating = ""

if number >= 90 and number <=100:
    rating = "Outstanding"
elif  number >=80 and number < 90:
    rating = "Exceeds Expectations"
elif number >=70 and number < 80:
    rating = "Meeting Expectations"  
elif number >=60 and number < 70:
    rating = "Below Expectations"
elif number >=0 and number < 60:
    rating = "Unsatisfactory"
else:
    rating = "Invalid score. Please enter a score between 0 and 100."

print(f"Employee Name: {name}")
print(f"Performance Score: {number}")
print(f"Performance Rating: {rating}")