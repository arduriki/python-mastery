data = ["a", "b", "c", "d", "e"]

# for-loops
# from 0 to 9 -> 10 exclusive
for i in range(10):
    print(i, end=" ")
    # i is increased here

print()

# from data's length
for i in range(len(data)):
    print(data[i], end=" ")

print()

for letter in data:
    print(letter, end=" ")

print()

# have an index and the data
for i, letter in enumerate(data):
    print(i, letter, end=" ")

print()

data_dictionary = {"Jimmy": 5, "Jordi": 10, "Monica": 12, "Caleb": 4}

# variation of the range function
for name in data_dictionary:
    print(name, end=" ")

print()

# ------------------
# While loops
data = ["a", "b", "c", "d", "e"]
i = 0

while i < len(data):
    print(data[i], end=" ")
    i += 1

print()

while True:
    x = input("Enter something: ")
    if x == "stop":
        break
    elif x == "special":
        # skips to the next iteration
        continue
    else:
        print("it wasn't stop or special")
    # this one works like the 'else' section
    print("printing data...")

print()

# not formatted output dictionary
print(data_dictionary)
# iterate through dictionaries
for (
    key,
    value,
) in data_dictionary.items():
    if key == "Jordi":
        print("Jordi is here.")
        break
    print(key, value)
