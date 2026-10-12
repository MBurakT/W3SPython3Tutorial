# Arguments
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
# The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name.
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
print()

# Parameters vs Arguments
# The terms parameter and argument can be used for the same thing: information that are passed into a function.
# From a function's perspective:
#   A parameter is the variable listed inside the parentheses in the function definition.
#   An argument is the actual value that is sent to the function when it is called.
def my_function(name):
    print("Hello", name) # name is a parameter

my_function("Emil")      # "Emil" is an argument 
print()

# Number of Arguments
# By default, a function must be called with the correct number of arguments.
# If your function expects 2 arguments, you must call it with exactly 2 arguments.
def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Refsnes")
print()

# Default Parameter Values
# You can assign default values to parameters. If the function is called without an argument, it uses the default value.
def my_function(name = "friend"):
    print("Hello", name)

my_function()
my_function("Emil")
my_function("Tobias")
my_function("Linus")
print()

# Keyword Arguments
# You can send arguments with the key = value syntax.
def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is ", name)

my_function(animal = "dog", name = "Buddy")
print()

# Positional Arguments
# When you call a function with arguments without using keywords, they are called positional arguments.
# Positional arguments must be in the correct order.
def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is ", name)

my_function("dog", "Buddy")
my_function("Buddy", "dog")
print()

# Mixing Positional and Keyword Arguments
# You can mix positional and keyword arguments in a function call.
# However, positional arguments must come before keyword arguments.
def my_function(animal, name, age):
    print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)
print()

# Passing Different Data Types
# You can send any data type as an argument to a function (string, number, list, dictionary, etc.).
# The data type will be preserved inside the function.
def my_function(fruits):
    for f in fruits:
        print(f)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)
print()

# Return Values
# Functions can return values using the return statement:
def my_function(x, y):
    return x + y

result = my_function(5, 3)
print(result)
print()

# Returning Different Data Types
def my_function():
    return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])
print()

# Positional-Only Arguments
# You can specify that a function can have ONLY positional arguments.
# To specify positional-only arguments, add , / after the arguments.
def my_function(name, /):
    print("Hello", name)

my_function("Emil")
print()

# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments.
def my_function(name):
    print("Hello", name)

my_function(name = "Emil") 
print()

# Keyword-Only Arguments
# To specify that a function can have only keyword arguments, add *, before the arguments.
def my_function(*, name):
    print("Hello", name)

my_function(name = "Emil")
print()

# Without *,, you are allowed to use positional arguments even if the function expects keyword arguments.
def my_function(name):
    print("Hello", name)

my_function("Emil")
print()

# Combining Positional-Only and Keyword-Only
# You can combine both argument types in the same function.
# Arguments before / are positional-only, and arguments after * are keyword-only:
def my_function(a, b, /, *, c, d):
    return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)
print()

