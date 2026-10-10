# Remove Specified Item
# The remove() method removes the specified item.
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.remove("banana")
print(thislist)
print()

# If there are more than one item with the specified value, the remove() method removes the first occurrence
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
print(thislist)
thislist.remove("banana")
print(thislist)
print()

# Remove Specified Index
# The pop() method removes the specified index.
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.pop(1)
print(thislist)
print()

# If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.pop()
print(thislist)
print()

# The del keyword also removes the specified index.
thislist = ["apple", "banana", "cherry"]
print(thislist)
del thislist[0]
print(thislist)
print()

# The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
print(thislist)
del thislist
# print(thislist)
print()

# Clear the List
# The clear() method empties the list.
# The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist.clear()
print(thislist)
print()

