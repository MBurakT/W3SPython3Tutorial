# What is PIP?
# PIP is a package manager for Python packages, or modules if you like.

# What is a Package?
# A package contains all the files you need for a module.
# Modules are Python code libraries you can include in your project.

# Check if PIP is Installed
# Navigate your command line to the location of Python's script directory, and type the following.
# cd C:\Users\mbtbr\AppData\Local\Programs\Python\Python314\Scripts
# pip --version

# Download a Package
# Downloading a package is very easy.
# Open the command line interface and tell PIP to download the package you want.
# Navigate your command line to the location of Python's script directory, and type the following:
# cd C:\Users\mbtbr\AppData\Local\Programs\Python\Python314\Scripts
# pip install camelcase

# Using a Package
import camelcase

c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))
print()

# Find Packages
# Find more packages at https://pypi.org/.

# Remove a Package
# Use the uninstall command to remove a package:
# cd C:\Users\mbtbr\AppData\Local\Programs\Python\Python314\Scripts
# pip uninstall camelcase

# List Packages
# Use the list command to list all the packages installed on your system.
# cd C:\Users\mbtbr\AppData\Local\Programs\Python\Python314\Scripts
# pip list

