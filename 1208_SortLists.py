# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default.
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
print(thislist)
thislist.sort()
print(thislist)
print()

thislist = [100, 50, 65, 82, 23]
print(thislist)
thislist.sort()
print(thislist)
print()

# Sort Descending
# To sort descending, use the keyword argument reverse = True
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
print(thislist)
thislist.sort(reverse = True)
print(thislist)
print()

thislist = [100, 50, 65, 82, 23]
print(thislist)
thislist.sort(reverse = True)
print(thislist)
print()

# Customize Sort Function
# You can also customize your own function by using the keyword argument key = function.
def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
print(thislist)
thislist.sort(key = myfunc)
print(thislist)
print()

# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
print(thislist)
thislist.sort()
print(thislist)
print()

# Luckily we can use built-in functions as key functions when sorting a list.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
print(thislist)
thislist.sort(key = str.lower)
print(thislist)
print()

# Reverse Order
# The reverse() method reverses the current sorting order of the elements.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
print(thislist)
thislist.reverse()
print(thislist)
print()

