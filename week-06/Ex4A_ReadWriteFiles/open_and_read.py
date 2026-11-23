f = open("about_me.txt", "r")

# Step 10: read the whole file
# print(f.read())

# Step 12: read 50 characters at a time
# print(f.read(50))
# print(f.read(50))

# Step 13: readline
# print(f.readline(10))
# print(f.readline())
# for i in range(1, 5):
#     print(f.readline())

# Step 14: readlines
# print(f.readlines(1))
# print(f.readlines(1))
# print(f.readlines(10))
# print(f.readlines(10))
# print(f.readlines(100))
# print(f.readlines(-1))

# Step 15-16: combine the read methods
first_50 = f.read(50)

next_lines = []
for i in range(1, 5):
    next_lines.append(f.readline())

next_100 = f.readlines(100)

print(f"First 50 characters: {first_50}")
print(f"Next four lines, as list by line: {next_lines}")
print(f"Next 100 characters, as list by line, rounded up to complete lines: {next_100}")

f.close()