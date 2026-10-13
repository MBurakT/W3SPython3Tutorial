# Python does not have built-in support for Arrays, but Python Lists can be used instead.

# Arrays
# This page shows you how to use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, like the NumPy library.
# Arrays are used to store multiple values in one single variable.
cars = ["Ford", "Volvo", "BMW"]
print(cars)
print()

# What is an Array?
# An array is a special variable, which can hold more than one value at a time.

# Access the Elements of an Array
# You refer to an array element by referring to the index number.
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)
cars[0] = "Toyota"
print(cars[0])
print()

# The Length of an Array
# Use the len() method to return the length of an array (the number of elements in an array).
cars = ["Ford", "Volvo", "BMW"]
print(len(cars))
print()

# Looping Array Elements
# You can use the for in loop to loop through all the elements of an array.
cars = ["Ford", "Volvo", "BMW"]
for i in cars:
    print(i)
print()

# Adding Array Elements
# You can use the append() method to add an element to an array.
cars = ["Ford", "Volvo", "BMW"]
print(cars)
cars.append("Honda")
print(cars)
print()

# Removing Array Elements
# You can use the pop() method to remove an element from the array.
cars = ["Ford", "Volvo", "BMW"]
print(cars)
cars.pop(1)
print(cars)
print()

# You can also use the remove() method to remove an element from the array.
cars = ["Ford", "Volvo", "BMW"]
print(cars)
cars.remove("Volvo")
print(cars)
print()

