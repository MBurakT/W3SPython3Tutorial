# range
# The built-in range() function returns an immutable sequence of numbers, commonly used for looping a specific number of times.
# This set of numbers has its own data type called range.

# Call range() With One Argument
x = range(5)
for i in x:
    print(i)
print()

# Call range() With Two Arguments
x = range(3, 5)
for i in x:
    print(i)
print()

# Call range() With Three Arguments
x = range(3, 10, 2)
for i in x:
    print(i)
print()

# Using ranges
# Ranges are often used in for loops to iterate over a sequence of numbers.
for i in range(5):
    print(i)
print()

# Using List to Display Ranges
# The range object is a data type that represents an immutable sequence of numbers, and it is not directly displayable.
# Therefore, ranges are often converted to lists for display.
print(list(range(5)))
print(list(range(1, 6)))
print(list(range(5, 20, 3)))
print()

# Slicing Ranges
# Like other sequences, ranges can be sliced to extract a subsequence.
r = range(10)
print(r[2])
print(r[:3])
print()

# Membership Testing
# Ranges support membership testing with the in operator.
r = range(0, 10, 2)
print(6 in r)
print(7 in r)
print()

# Length
# Ranges support the len() function to get the number of elements in the range.
r = range(0, 10, 2)
print(len(r))
print()

