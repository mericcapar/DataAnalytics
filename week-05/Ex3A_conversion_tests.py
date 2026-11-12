# Description: This script tests various numeric
# conversion techniques
# Author: Sam Q. Newprogrammer

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# a) Cast as integer using int()
# a_int = int(a)  # ValueError: "101.1" has a decimal point
b_int = int(b)  # Works: 55
# c_int = int(c)  # ValueError: the string contains letters
# d_int = int(d)  # ValueError: the string contains letters

# b) Cast as float using float()
a_float = float(a)  # Works: 101.1 (spaces around it are ignored)
b_float = float(b)  # Works: 55.0
# c_float = float(c)  # ValueError: the string contains letters
# d_float = float(d)  # ValueError: the string contains letters

# c) For a, cast to float first, then to integer
a_float_int = int(float(a))  # Works: 101 (the decimal part is dropped)

# d) Slicing: keep only the numeric part of each string
a_slice = float(a[1:6])  # "101.1" -> 101.1 (float, it has a decimal)
b_slice = int(b[0:2])  # "55" -> 55
c_slice = int(c[0:3])  # "402" -> 402
d_slice = int(d[7])  # "5" -> 5

print(b_int, type(b_int))
print(a_float, type(a_float))
print(b_float, type(b_float))
print(a_float_int, type(a_float_int))
print(a_slice, type(a_slice))
print(b_slice, type(b_slice))
print(c_slice, type(c_slice))
print(d_slice, type(d_slice))

# e) Remove leading and trailing spaces with .strip()
print(a.strip(), type(a.strip()))  # "101.1", still a string
print(d.strip(), type(d.strip()))  # "Number 5", still a string