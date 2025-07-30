# Lists
data = ["Jordi", "Caleb"]
print(data[0])

data.append("Jimmy")
# nested list
data.append(["hello"])
data.append(5)

print(data)

data = ["Jimmy", "Jordi", "Monica", "Samantha"]
# slicing a list - last index isn't included
print(data[1:3])
# from the beginning
print(data[:3])
# to the end
print(data[1:])
# step
print(data[1:4:2])

# Sets: it doesn't allow to duplicate data
data = {"Jimmy", "Jordi", "Monica", "Samantha", "Jordi"}

# Dictionaries
data_dictionary = {"Jimmy": 5, "Jordi": 10, "Monica": 12, "Caleb": 4}


print(data)
print(data_dictionary)
# Get a value from a dictionary
print(data_dictionary.get("Jordi"))
