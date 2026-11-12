import math

#Formula: square root of ((x2 - x1)^2 + (y2 - y1)^2)
x1 = 1
x2 = 2
y1 = 3
y2 = 4

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is "
      f"{distance:.2f}")