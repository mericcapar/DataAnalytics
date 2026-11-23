# ValueError: converting text that isn't a number
try:
    number = int("hello")
except ValueError:
    print("ValueError: That text can't be converted to a number.")
else:
    print(number)
finally:
    print("Let's try another one...\n")

# ValueError: unpacking the wrong number of values
try:
    a, b = [1, 2, 3]
except ValueError:
    print("ValueError: The number of variables doesn't match the number of values.")
else:
    print(a, b)
finally:
    print("Let's try another one...\n")

# NameError: using a variable that was never defined
try:
    m = banana
except NameError:
    print("NameError: Oops, looks like you tried to use an undefined variable.")
else:
    print(m)
finally:
    print("Let's try another one...\n")

# TypeError (1): adding a string and a number
try:
    result = "Age: " + 25
except TypeError:
    print("TypeError: You can't add a string and a number together.")
else:
    print(result)
finally:
    print("Let's try another one...\n")

# TypeError (2): calling a function with the wrong number of arguments
try:
    result = len("a", "b")
except TypeError:
    print("TypeError: That function got the wrong number of arguments.")
else:
    print(result)
finally:
    print("Let's try another one...\n")

# SyntaxError: a real syntax error stops the whole file before it runs,
# so we put the broken code in a string and run it with eval()
try:
    result = eval("5 +* 3")
except SyntaxError:
    print("SyntaxError: That code isn't written correctly.")
else:
    print(result)
finally:
    print("Let's try another one...\n")