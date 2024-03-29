# Student Name: Zihua Li
# Assignment 2.1: Personal Multi-Calculator
'''
The purpose of this script: a calculator that addresses the user, asks the user for
two numbers, then does a bunch of operations, and prints out the results to the user.
'''
# Citation: No help from others received or used any resources to accomplish this assignment.

# Entering username
username = input("Please enter your name: ")

# Greeting message
print("Hi",username,", welcome to Personal Multi- Calculator!")

# Data input
first_num = float(input("Please enter your first number: "))
second_num = float(input("Please enter your second number: "))

# The four operations & preventing error (division by zero)
sum = first_num + second_num
subtraction = first_num - second_num
product = first_num * second_num
if second_num == 0:
    quotient = "A number cannot be divided by zero!"
else:
    quotient = first_num / second_num

# Judging if results are whole numbers, if true, turn them into integers
if sum % 1 == 0:
    sum = int(sum)
if subtraction % 1 == 0:
    subtraction = int(subtraction)
if product % 1 == 0:
    product = int(product)
'''
Preventing error, if second_num is zero, quotient will be an error message
If quotient is an error message, int(quotient) will cause error
'''
if second_num != 0:
    if quotient % 1 == 0:
        quotient = int(quotient)
    
# Printing out the results of the four operations
print("The sum of two numbers is: ",sum)
print("The difference of two numbers is: ",subtraction)
print("The product of two numbers is: ",product)
print("The quotient of two numbers is: ",quotient)
