# For Loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
fruits = ["apple", "banana", "cherry"]
for i in fruits:
    print(i)
print()

# Looping Through a String
for i in "banana":
    print(i)
print()

# The break Statement
# With the break statement we can stop the loop before it has looped through all the items.
fruits = ["apple", "banana", "cherry"]
for i in fruits:
    if i == "banana":
            break
    print(i)
    
print()

#  The continue Statement
# With the continue statement we can stop the current iteration of the loop, and continue with the next.
fruits = ["apple", "banana", "cherry"]
for i in fruits:
     if i == "banana":
          continue
     print(i)
print()

# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function, The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for i in range(1, 10, 3):
     print(i)
print()

# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished.
for i in range(6):
     print(i)
else:
     print("Finally finished!")
print()

# Nested Loops
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop".
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
     for y in fruits:
          print(x, y)
print()

# The pass Statement
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for i in [0, 1, 2]:
     pass

