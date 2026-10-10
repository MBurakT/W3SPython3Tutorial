# Copy a List
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
# You can use the built-in List method copy() to copy a list.
thislist = ["apple", "banana", "cherry"]
print(thislist)
mylist = thislist.copy()
print(mylist)
print()

# Another way to make a copy is to use the built-in method list().
thislist = ["apple", "banana", "cherry"]
print(thislist)
mylist = list(thislist)
print(mylist)
print()

# Use the slice Operator
# You can also make a copy of a list by using the : (slice) operator.
thislist = ["apple", "banana", "cherry"]
print(thislist)
mylist = thislist[:]
print(mylist)
print()

