# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
mytuple = ("apple", "banana", "cherry")

thistuple = ("apple", "banana", "cherry")
print(thistuple)
print()


# Tuples can also be created without the parentheses.
thistuple = "apple", "banana", "cherry"
print(thistuple)
print()

# Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values.


# Ordered
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.


# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.


# Allow Duplicates
# Since tuples are indexed, they can have items with the same value.

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print()

# Tuple Lenght
# To determine how many items a tuple has, use the len() function.
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
print()

# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)
print(type(thistuple))

thistuple = ("apple")
print(type(thistuple))
print()

# Create an Empty Tuple
# To create an empty tuple, use round brackets with no content.
thistuple = ()
print(type(thistuple))
print()

# Tuple Items - Data Types
# Tuple items can be of any data type.
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)
print()

# A tuple can contain different data types.
tuple1 = ("abc", 34, True, 40, "male")
print(tuple)
print()

# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)
print()

