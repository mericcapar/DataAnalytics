time = int(input("What time is it? (0-23) "))

if time < 0 or time > 23:
    print("Invalid time.")
elif time >= 23 or time < 4:
    print("What are you doing up so late??")
elif time < 10:
    print("Good morning!")
elif time < 17:
    print("Good day!")
else:
    print("Good evening!")