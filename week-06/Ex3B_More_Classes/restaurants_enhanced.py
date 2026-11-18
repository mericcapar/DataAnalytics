class Restaurant:
    '''Represents a restaurant, tracks customers served and customer ratings.'''

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

    def add_num_served(self):
        served = int(input("How many customers served today? "))
        self.number_served += served

    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers")

    def customer_rating(self):
        while True:
            rating = input("How would you rate your experience today on a scale of 1-5 (5 being excellent)? ")
            if rating.isdigit() and 1 <= int(rating) <= 5:
                break
            print("Please enter a whole number from 1 to 5.")
        rating = int(rating)
        self.customer_ratings.append(rating)
        average = sum(self.customer_ratings) / len(self.customer_ratings)
        print(f"Your rating was {rating}. The average rating for this restaurant is {average:.1f}")


restaurant1 = Restaurant("Cafe Baklava", "Turkish food")
restaurant2 = Restaurant("Asian Kitchen", "Japanese food")
restaurant3 = Restaurant("Zareen's", "Indian food")

for restaurant in [restaurant1, restaurant2, restaurant3]:
    print(f"\n=== {restaurant.rest_name} ===")
    restaurant.print_num_served()
    restaurant.add_num_served()
    restaurant.add_num_served()
    restaurant.print_num_served()
    restaurant.customer_rating()
    restaurant.customer_rating()