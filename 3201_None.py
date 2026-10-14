# None
# None is a special constant in Python that represents the absence of a value.
# Its data type is NoneType, and None is the only instance of a NoneType object.

# NoneType
# Variables can be assigned None to indicate "no value" or "not set".
x = None
print(x)
print(type(x))
print()

# Comparing to None
# To compare a value to None, use the identity operator is or is not
result = None
if result is None:
    print("No result yet")
else:
    print("Reult is ready")
print()

# True or False
# None evaluates to False in a boolean context.
print(bool(None))
print()

# Functions returning None
# Functions that do not explicitly return a value return None by default.

def myfunc():
    x = 5

x = myfunc()
print(x)
print()

