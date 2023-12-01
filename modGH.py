# 7.4 Python Modules
# HINT: https://www.w3schools.com/python/python_modules.asp
# HINT: https://realpython.com/python-modules-packages/
# HINT: https://docs.python.org/3/tutorial/modules.html


# 7.4.1 Create a python module mod.
# In mod.py, create a function psum(number1, number2) that takes two arguments and prints the sum of them. Assume the input arguments to be numbers.
def psum(number1, number2):
    print('sum of numbers :', number1+number2)

# In mod.py, create a function pmultiply(number1, number2) that takes two arguments and prints the product of them. Assume the input arguments to be numbers.
def pmultiply(number1, number2):
    print('product of numbers:', number1*number2)

# 7.4.2 Create python file main.py and import the module mod.
# In main.py run the psum() and pmultiply() functions from the module mod using any two numbers.


# 7.4.3 In main.py, also import Python's built in module platform. Then list the functions and variables in the platform module using the dir() function.
