# Join Two Lists
# There are several ways to join, or concatenate, two or more lists in Python.
# One of the easiest ways are by using the + operator.
list1 = ["a", "b", "c", "d"]
list2 = [1, 2, 3]

list3 = list2 + list1
print(list3)
print()

# Another way to join two lists is by appending all the items from list2 into list1, one by one.
list1 = ["a", "b", "c", "d"]
list2 = [1, 2, 3]

for i in list2:
    list1.append(i)

print(list1)
print()

# Or you can use the extend() method, where the purpose is to add elements from one list to another list.
list1 = ["a", "b", "c", "d"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
print()

