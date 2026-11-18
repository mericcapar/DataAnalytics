import random

products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
            'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp', 'Surge Protector']

# pick one random item
product_of_the_day = random.choice(products)
print(f"Product of the Day: {product_of_the_day}")

# b) pick 3 different items with no repeat items
survey_products = random.sample(products, 3)
print(f"Survey products: {survey_products}")

# c) shuffle the list in place
random.shuffle(products)
print(f"Shuffled products: {products}")

# d) Simulated daily transaction count between 50 and 300
transactions = random.randint(50, 300)
print(f"Daily transaction count: {transactions}")