'''
Student Name: Zihua Li
Assignment 3.1: Calculator Shell
This is a shell that takes in user commands, requests operands, and executes operations.
Citation: "Check if string is a real number" [https://stackoverflow.com/questions/5956240/check-if-string-is-a-real-number/5956309]
           used the answer by 'orlp' & 'wim' for reference, in line 10 to line 23
'''

# Supporting sys.exit()
import sys

# Defining a function to check if input is a float number
def isfloat(input):
    try:
        float(input)
    except ValueError: 
        return False
    return True

# Defining a function to check if input is an integer
def isinteger(input):
    try:
        int(input)
    except ValueError:
        return False
    return True

# Greeting the user
print("Welcome to the calculator shell.")
print("Available commands: add, subtract, divide, multiply, squared, cubed, help, exit")

# A while loop that prompts user input at the beginning of each loopand only breaks out when the user exits.
exit_indicator = 0
while exit_indicator == 0:

    # User input: command
    command = input()

    # If user input command is "add" or "subtract" or "divide" or "multiply", which these operations require 2 operands
    if command == "add" or command == "subtract" or command == "divide" or command == "multiply":

        # Requesting first & second operands & preventing false input
        first_operand = input("Please enter the first operand: ")
        while isfloat(first_operand) == False:
            print("Invalid operand.")
            first_operand = input("Please enter the first operand: ")
        else:
            second_operand = input("Please enter the second operand: ")
            while isfloat(second_operand) == False:
                print("Invalid operand.")
                second_operand = input("Please enter the second operand: ")
            else:
                first_operand = float(first_operand)
                second_operand = float(second_operand)
                # If user requested "add" operation
                if command == "add":
                    sum = (first_operand + second_operand)
                    print("The sum of",first_operand,"and",second_operand,"is",sum)

                # If user requested "subtract" operation
                elif command == "subtract":
                    difference = first_operand - second_operand
                    print("The difference of",first_operand,"minus",second_operand,"is",difference)

                # If user requested "divide" operation & preventing divided by zero
                elif command == "divide":
                    while second_operand == 0 or isfloat(second_operand) == False:
                        print("You cannot divide by zero.")
                        second_operand = input("Please enter the second operand: ")
                        while isfloat(second_operand) == False:
                            print("Invalid operand.")
                            second_operand = input("Please enter the second operand: ")
                        else:
                            second_operand = float(second_operand)
                    else:
                        quotient = first_operand // second_operand
                        print("The quotient of",first_operand,"divided by",second_operand,"is",quotient)

                # If user requested "multiply" operation
                elif command == "multiply":
                    product = first_operand * second_operand
                    print("The product of",first_opearand,"multiply by",second_operand,"is",product)

    # If user requested "squared" or "cubed" operation
    elif command == "squared" or command == "cubed":

        # Requesting the operand & preventing false input
        operand = input("Please enter the operand: ")
        while isinteger(operand) == False:
            print("Invalid operand.")
            operand = input("Please enter the operand: ")
        else:
            operand = int(operand)
            while operand <= 0:
                print("Invalid operand.")
                operand = input("Please enter the operand: ")
            else:
                operand = float(operand)
                if command == "squared":
                    square = operand * operand
                    print("The square of",operand,"is",square)
                else:
                    cube = operand * operand * operand
                    print("The cube of",operand,"is",cube)
            
    # If user entered "help" or "exit" command
    elif command == "help" or command == "exit":
        if command == "help":
            print("The available commands are: add, subtract, divide, multiply, squared, cubed, help, exit.")
        else:
            exit_indicator = 1

    # If user entered other unknown command
    else:
        print("Command not found, please enter a valid command.")
else:
    sys.exit("Thank you for using the calculator shell! Ending program.")
        
