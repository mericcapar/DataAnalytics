import random

random_number = random.randint(1, 100)
try_count = 0

print("Guess my number (1-100). You have 5 guesses.")

while True:
    guess = int(input("Your guess: "))
    try_count += 1

    if guess == random_number:
        print(f"Correct! The number was {random_number}")
        print(f"It took you {try_count} guesses.")
        break

    if try_count == 5:
        print(f"Game over! The number was {random_number}")
        break

    if guess < random_number:
        print("Higher!")
    else:
        print("Lower!")
    print(f"{5 - try_count} guesses left!")