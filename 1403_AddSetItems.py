# Add Items
# To add one item to a set use the add() method.
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset.add("orange")
print(thisset)
print()

# Add Sets
# To add items from another set into the current set, use the update() method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
print(thisset)
thisset.update(tropical)
print(thisset)
print()

# Add Any Iterable
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
print(thisset)
thisset.update(mylist)
print(thisset)
print()

