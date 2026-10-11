# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.remove("banana")
print(thisset)
print()

# If the item to remove does not exist, remove() will raise an error.
# If the item to remove does not exist, discard() will NOT raise an error.
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.discard("banana")
print(thisset)
print()

# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
# The return value of the pop() method is the removed item.
thisset = {"apple", "banana", "cherry"}
print(thisset)
x = thisset.pop()
print(x)
print(thisset)
print()

thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.clear()
print(thisset)
print()

thisset = {"apple", "banana", "cherry"}
print(thisset)
del thisset
# print(thisset)
print()
