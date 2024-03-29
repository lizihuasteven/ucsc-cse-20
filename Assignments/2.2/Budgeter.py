# Student Name: Zihua Li
# Assignment 2.2: Simple Budgeter
'''
a simple budgeting tool that asks for your budget, how much you spent,
and then tells you how much you have left and if you've spent too much. 
'''
# Citation: No help from others received or used any resources to accomplish this assignment.

# Entering username & greeting & entering budget
username = input("Hello! Please enter your name: ")
print("Hi",username,", please enter your budget (in dollars): ",end="")
budget = float(input(""))

# Showing entered budget & entering the amount of money spent
print("Your budget is $",budget,". Please enter how much you spent: ",sep="",end="")
spent = float(input(""))

# Judging if their spent is within their budget, also report how much left or overspent
if spent > budget:
    amount_overspent = spent - budget
    print("Oh no! you went over your budget! You have overspent by $",amount_overspent,sep="")
else:
    amount_left = budget - spent
    print("Good! Your spent is with in your budget, you have $",amount_left," left in your budget.",sep="")
