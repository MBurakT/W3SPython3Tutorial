# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for i in fruits:
    if("a" in i):
        newlist.append(i)
print(newlist)
print()


# With list comprehension you can do all that with only one line of code.
# newlist = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [i for i in fruits if "a" in i]
print(newlist)
print()

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
print(fruits)
newlist = [i for i in fruits]
print(newlist)
newlist = [i for i in fruits if "apple" != i]
print(newlist)
print()

# Iterable
# The iterable can be any iterable object, like a list, tuple, set etc.
# You can use the range() function to create an iterable.
newlist = [i for i in range(10)]
print(newlist)
print()

newlist = [i for i in range(10) if(i % 2 == 0)]
print(newlist)
print()

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [i.upper() for i in fruits]
print(newlist)
print()

newlist = ['hello' for i in range(5)]
print(newlist)
print()

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [i if i != "banana" else "orange" for i in fruits]
print(newlist)
print()

