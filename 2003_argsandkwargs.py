# *args and **kwargs
# By default, a function must be called with the correct number of arguments. 
# However, sometimes you may not know how many arguments that will be passed into your function.
# *args and **kwargs allow functions to accept a unknown number of arguments.

# Arbitrary Arguments - *args
# If you do not know how many arguments will be passed into your function, add a * before the parameter name.
# This way, the function will receive a tuple of arguments and can access the items accordingly
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
print()

# Arbitrary Arguments are often shortened to *args in Python documentation.

# What is *args?
# The *args parameter allows a function to accept any number of positional arguments.
# Inside the function, args becomes a tuple containing all the passed arguments.
def my_function(*args):
    print("Type:", type(args))
    print("First argument", args[0])
    print("Second argument", args[1])
    print("All argument", args)

my_function("Emil", "Tobias", "Linus")
print()

# Using *args with Regular Arguments
# You can combine regular parameters with *args.
# Regular parameters must come before *args:
def my_function(greeting, *names):
    for name in names:
        print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")
print()

# Practical Example with *args
# *args is useful when you want to create flexible functions.
def my_function(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(my_function())
print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))
print()

def my_function(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(my_function(3, 7, 2, 9, 1))
print()

# Arbitrary Keyword Arguments - **kwargs
# If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.
# This way, the function will receive a dictionary of arguments and can access the items accordingly.
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
print()

# What is **kwargs?
# The **kwargs parameter allows a function to accept any number of keyword arguments.
# Inside the function, kwargs becomes a dictionary containing all the keyword arguments.
def my_function(**myvar):
    print("Type:", type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")
print()

# Using **kwargs with Regular Arguments
# You can combine regular parameters with **kwargs.
# Regular parameters must come before **kwargs:
def my_function(username, **details):
    print("Username:", username)
    print("Additional details:")
    for key, value in details.items():
        print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")
print()

# Combining *args and **kwargs
# You can use both *args and **kwargs in the same function.
# The order must be: 1.regular parameters 2.*args 3.**kwargs
def my_function(title, *args, **kwargs):
    print("Title:", title)
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")
print()

# Unpacking Arguments
# The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments.
# Unpacking Lists with *
# If you have values stored in a list, you can use * to unpack them into individual arguments:
def my_function(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)
print()

# Unpacking Dictionaries with **
# If you have keyword arguments stored in a dictionary, you can use ** to unpack them.
def my_function(fname, lname):
    print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")
print()

