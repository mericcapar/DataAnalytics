cities = ["Istanbul","Tokyo", "Barcelona", "New York", "Seoul"]

for number, city in enumerate(cities, start=1):
    if number == 1:
        print(f"{number}. {city} <- top pick!")
    else:
        print(f"{number}. {city}")


print()
for number, city in enumerate(reversed(cities), start=1):
    print(f"{number}. {city}")

    