#1getting_started.py

# 1. Syntax

# 1.1 Insert the missing indentation to make the code correct:
# HINT: https://www.w3schools.com/python/python_syntax.asp

# TODO: update the code below
if 4 == 2:
    print("Four is equal to two!")



# 1.2 Variables
# HINT: https://www.w3schools.com/python/python_variables.asp

#1.2.1 Create a variable named fruit and assign the value Apple to it.
# TODO: Write your code below
fruit = "Apple"


# 1.2.2 Create a variable called z, assign x + y to it, and display the result.


# TODO: Wrtie your code below
x = 10
y = 20
z = x + y
print(z)



# 1.2.3 Remove the illegal characters in the variable name:

# TODO: Update the code below
city_name = "London"

# 1.2.4 Insert the correct keyword to make the variable x belong to the global scope.
# HINT: https://www.w3schools.com/python/python_variables_global.asp

# TODO: Update the code below
def myfunc():
  global x
  x = "fantastic"



# 1.2.5 write a program that switches the values stored in variables a and b.

a = 5
b = 4

temp = a
a = b
b = temp

print('a: ', a)
print('b: ', b)

# TODO: Write your code below

print('a : ',a)
print('b : ',b)


# 1.3. Data Types
# casting, numbers, booleans
# HINT: https://www.w3schools.com/python/python_datatypes.asp

# 1.3.1 Write a program that add the digits in a two digit number input.
# eg. if the input is 45. The the output should be 4+5=9

# TODO: Wrtie your code below

number = input("Enter a two-digit number: ")
digit_sum = int(number[0]) + int(number[1])
print("Sum of digits:", digit_sum)

