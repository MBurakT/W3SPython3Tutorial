# Logical Operators
# Logical operators are used to combine conditional statements. Python has three logical operators: and, or, not 
# The and Operator
# The and keyword is a logical operator, and is used to combine conditional statements. Both conditions must be true for the entire expression to be true.
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are true")
print()

# The or Operator
# The or keyword is a logical operator, and is used to combine conditional statements. At least one condition must be true for the entire expression to be true.
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")
print()

# The not Operator
# The not keyword is a logical operator, and is used to reverse the result of the conditional statement.
a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")
print()

# Combining Multiple Operators
# You can combine multiple logical operators in a single expression. Python evaluates not first, then and, then or.
age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
    print("Discount applies!")
print()

