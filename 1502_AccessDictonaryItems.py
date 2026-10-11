# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets.
# There is also a method called get() that will give you the same result.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
# x = thisdict.get("model")
print(x)
print()

# Get Keys
# The keys() method will return a list of all the keys in the dictionary.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.keys()
print(x)
print()

# The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
print(x)
car["color"] = "white"
print(x)
print()

# Get Values
# The values() method will return a list of all the values in the dictionary.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = thisdict.values()
print(x)
print()

# The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x)
car["year"] = 2020
print(x)
print()

# Add a new item to the original dictionary, and see that the values list gets updated as well.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x)
car["color"] = "red"
print(x)
print()

# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = thisdict.items()
print(x)
print(type(x))
print()

# The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x)
car["year"] = 2020
print(x)
print()

# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
    print("Yes")
print()

