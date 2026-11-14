# #Class Exercise 1
# classmate_1 = 'Moses Jura'
# classmate_2 = 'Ardita Mrapshtija'

# print(f"My classmate {classmate_1}.")
# print(f"My favorite classmate is {classmate_2}.")

# #Class Exercise 2

# item_1= 25.75
# item_2= 45.67
# item_3=45.75
# item_4=55.67
# item_5=45.60

# sales_tax=0.07

# Sub_total= item_1 + item_2 + item_3 + item_4 + item_5
# total_sales_tax= Sub_total * sales_tax
# total= Sub_total + total_sales_tax

# print(f"Sub Total: ${Sub_total:.2f}")
# print(f"Sales Tax: ${total_sales_tax:.2f}")
# print(f"Total: ${total:.2f}")

# #Exercise 3

# celcius = 35
# transformed_fahrenheit = (celcius * 9/5) + 32
# print(f"{celcius} degrees Celsius is equal to {transformed_fahrenheit} degrees Fahrenheit.")

# #Exercise 4

# cost = float(input("Enter the cost of the meal: "))
# tip = cost * 0.20
# tax = cost * 0.0825
# total_cost = cost + tip + tax
# print('------Meal Cost Breakdown------')
# print(f"{'Meal Cost:':<15}${cost:>6.2f}")
# print(f"{'Tip (20%):':<15}${tip:>6.2f}")
# print(f"{'Tax (8.25%):':<15}${tax:>6.2f}")
# print('--------------------------------')
# print(f"{'Total Cost:':<15}${total_cost:>6.2f}")

# #Exercise 5
# name = input("Enter your name: ")
# number_1 = float(input("Enter the first number: "))
# number_2 = float(input("Enter the second number: "))
# number_3 = float(input("Enter the third number: "))

# average = (number_1 + number_2 + number_3) / 3

# print(f"Hello {name} ! The average of {number_1}, {number_2}, and {number_3} is {average:.2f}.")


monday = 1200
tuesday = 1500
wednesday = 1100
thursday = 1800
friday = 1400

total_sales = 0
average_sales = 0
i = 0

# while i < 5:
#     total_sales = monday + tuesday + wednesday + thursday + friday
#     average_sales = total_sales / 5
#     i += 1
# print(f"Total sales for the week: ${total_sales:.2f}")
# print(f"Average sales for the week: ${average_sales:.2f}")

# for i in range(5):
#     if day == 1:
#         total_sales += monday
#     elif day == 2:
#         total_sales += tuesday
#     elif day == 3:
#         total_sales += wednesday
#     elif day == 4:
#         total_sales += thursday
#     else:
#         total_sales += friday
#     day += 1  
# average_sales = total_sales / 5

# print(f"Total Sales: ${total_sales:,.2f}")
# print(f"Average Daily Sales: ${average_sales:,.2f}")

monthly_sales = [125000.50, 14200.75, 11800.25, 15600.00, 16250.50, 17500.80]
months = ['January', 'February', 'March', 'April', 'May', 'June']

#Task 2

for number, month in enumerate(months, start=1):
    print(f"Month {number}: {month}")

print('-----------------------------')
#Task 3
#  
for number, sales in enumerate(monthly_sales, start=1):
    print(f"Month {number}: ${sales:,.2f}")

    