# Decorators let you add extra behavior to a function, without changing the function's code.
# A decorator is a function that takes another function as input and returns a new function.

# Basic Decorator
# Define the decorator first, then apply it with @decorator_name above the function.
def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunction():
    return "Hello Sally"

print(myfunction())
print()

# Multiple Decorator Calls
# A decorator can be called multiple times. Just place the decorator above the function you want to decorate.
def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunction():
    return "Hello Sally"

@changecase
def outerfunction():
    return "I am speed!"

print(myfunction())
print(outerfunction())
print()

# Arguments in the Decorated Function
# Functions that require arguments can also be decorated, just make sure you pass the arguments to the wrapper function.
def changecase(func):
    def myinner(x):
        return func(x).upper()
    return myinner

@changecase 
def myfunction(name):
    return "Hello " + name

print(myfunction("John"))
print()

# *args and **kwargs
# Sometimes the decorator function has no control over the arguments passed from decorated function, to solve this problem, add (*args, **kwargs) to the wrapper function, this way the wrapper function can accept any number, and any type of arguments, and pass them to the decorated function.
def changecase(func):
    def myinner(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return myinner

@changecase
def myfunction(name):
    return "Hello " + name

print(myfunction("John"))
print()

# Decorator With Arguments
# Decorators can accept their own arguments by adding another wrapper level.
def changecase(n):
    def changecase(func):
        def myinner():
            if n == 1:
                a = func().lower()
            else:
                a = func().upper()
            return a
        return myinner
    return changecase

@changecase(1)
def myfunction():
    return "Hello Linus"

print(myfunction())
print()

# Multiple Decorators

def changecase(func):
    def myinner():
        return func().upper()
    return myinner

def addgreeting(func):
    def myinner():
        return "Hello " + func() + " Have a good day!"
    return myinner

@changecase
@addgreeting
def myfunction():
    return "Tobias"

print(myfunction())
print()

# Preserving Function Metadata
# Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.
def myfunction():
    return "Have a great day!"

print(myfunction.__name__)
print()

