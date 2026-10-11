# Loop Through a Dictionary
# You can loop through a dictionary by using a for loop
# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for i in thisdict:
    print(i, thisdict[i])
print()

# You can also use the values() method to return values of a dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for i in thisdict.values():
    print(i)
print()

# You can use the keys() method to return the keys of a dictionary.
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for i in thisdict.keys():
    print(i)
print()

# Loop through both keys and values, by using the items() method.
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
    print(x, y)
print()

