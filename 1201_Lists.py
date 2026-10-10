# Listlere birden fazla değeri tek bir değişkende saklamak için kullanılır.
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print("Listenin uzunluğu:", len(thislist))
print(type(thislist))
print()

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

list1 = ["abc", 34, True, 40, "male"]

thislist = list(("apple", "banana", "cherry"))
print(type(thislist))
print()

"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members
"""