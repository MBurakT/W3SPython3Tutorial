# What is a Virtual Environment?
# A virtual environment in Python is an isolated environment on your computer, where you can run and test your Python projects.
# It allows you to manage project-specific dependencies without interfering with other projects or the original Python installation.
# Think of a virtual environment as a separate container for each Python project. Each container:
#   Has its own Python interpreter
#   Has its own set of installed packages
#   Is isolated from other virtual environments
#   Can have different versions of the same package
# Using virtual environments is important because:
#   It prevents package version conflicts between projects
#   Makes projects more portable and reproducible
#   Keeps your system Python installation clean
#   Allows testing with different Python versions

# Creating a Virtual Environment
# Python has the built-in venv module for creating virtual environments.
# To create a virtual environment on your computer, open the command prompt, and navigate to the folder where you want to create your project, then type this command:
# C:\Users\mbtbr\Desktop\W3SPython3Tutorial>python -m venv myfirstproject

# Activate Virtual Environment
# To use the virtual environment, you have to activate it with this command:
# C:\Users\mbtbr\Desktop\W3SPython3Tutorial>myfirstproject\Scripts\activate

# Install Packages
# Once your virtual environment is activated, you can install packages in it, using pip.
# We will install a package called 'cowsay':
# (myfirstproject) C:\Users\mbtbr\Desktop\W3SPython3Tutorial>pip install cowsay

# Using Package
# Now that the 'cowsay' module is installed in your virtual environment, lets use it to display a talking cow.
import cowsay

cowsay.cow("Good Mooooorning!")
# (myfirstproject) C:\Users\mbtbr\Desktop\W3SPython3Tutorial>python 3401_VirtualEnvironment.py

# Deactivate Virtual Environment
# To deactivate the virtual environment use this command:
# (myfirstproject) C:\Users\mbtbr\Desktop\W3SPython3Tutorial>deactivate

# Delete Virtual Environment
# Another nice thing about working with a virtual environment is that when you, for some reason want to delete it, there are no other projects depend on it, and only the modules and files in the specified virtual environment are deleted.
# To delete a virtual environment, you can simply delete its folder with all its content. Either directly in the file system, or use the command line interface like this:
# C:\Users\mbtbr\Desktop\W3SPython3Tutorial>rmdir /s /q myfirstproject
