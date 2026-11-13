candies = ("Gummy Bears", "Lollipops", "Jelly Beans")
flavors = ("Strawberry", "Mango", "Watermelon")

# A set of candy and flavor combinations, using each tuple's index
candy_options = {
    flavors[0] + " " + candies[0],
    flavors[1] + " " + candies[1],
    flavors[2] + " " + candies[2],
    flavors[1] + " " + candies[0],
}

print("Today's candy options include:", candy_options)
print("Today's candy options include:", candy_options)
print("Today's candy options include:", candy_options)

# Sets are unordered, so the order of the items can change each time
# the script runs. Within the same run, the order usually stays the
# same, but running the script again may show a different order.