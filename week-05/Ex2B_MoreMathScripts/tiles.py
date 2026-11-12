import math

tiles_per_box = 12
length = int(input("Enter the length of the room in feet: "))
width = int(input("Enter the width of the room in feet: "))


tiles_needed = length * width

# math.ceil() rounds up.
boxes_needed = math.ceil(tiles_needed / tiles_per_box)
#print(boxes_needed)

# Buy at least 10% more.
tiles_with_extra = math.ceil(tiles_needed * 1.15)
boxes_to_buy = math.ceil(tiles_with_extra / tiles_per_box)
#print(boxes_to_buy)

print(f"The room needs {tiles_needed} tiles, or {boxes_needed} boxes.")
print(f"With 15% extra, you need {tiles_with_extra} tiles, "
      f"so you will buy {boxes_to_buy} boxes.")