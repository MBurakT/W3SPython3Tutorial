# What is a Module?
# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.

# Use a Module
# Now we can use the module we just created, by using the import statement:
import mymodule2401

mymodule2401.greeting("Burak")
print()

a = mymodule2401.person1["age"]
print(a)
print()

import mymodule2401 as mx

a = mx.person1["age"]
print(a)
print()

# Built-in Modules
# There are several built-in modules in Python, which you can import whenever you like.
import platform

x = platform.system()
print(x)
print()

# Using the dir() Function
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function.
import platform

x = dir(platform)
print(x)
print()

from mymodule2401 import person1

print (person1["age"])
print()

