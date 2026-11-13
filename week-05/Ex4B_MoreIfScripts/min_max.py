a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter a third number: "))
smallest = 0
biggest = 0

if a == b and a == c:
    smallest = a
    biggest = a

if a < b and a < c:
    smallest = a
elif b < a and b < c:
    smallest = b
elif c < a and c < b:
    smallest = c

if a > b and a > c:
    biggest = a
elif b > a and b > c:
    biggest = b
elif c > a and c > b:
    biggest = c

print(f"{smallest} is the smallest number.")
print(f"{biggest} is the largest number.")
