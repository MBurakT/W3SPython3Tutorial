# Short Hand If
a = 5
b = 2
if a > b : print("a is greater than b")
print()

# Short Hand If ... Else
# If you have one statement for if and one for else, you can put them on the same line using a conditional expression.
a = 2
b = 330
print("A") if a > b else print("B")
print()

# Assign a Value With If ... Else
# You can also use a one-line if/else to choose a value and assign it to a variable.
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)
print()

# Multiple Conditions on One Line
# You can chain conditional expressions, but keep it short so it stays readable.
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
print()

