'''
Student Name: Zihua Li
Assignment 3.2: Numbers Toolbox
This is a script that implements the following functions:
is_prime, LCM, convert_temp, and get_euclidean_dist.
Citation: No help from others received or used any resources to accomplish this assignment.
'''

# Defining a function to check if input is an integer
def isinteger(input):
    try:
        int(input)
    except ValueError:
        return False
    return True

# Defining a function to check if input is a float number
def isfloat(input):
    try:
        float(input)
    except ValueError:
        return False
    return True

# Defining a function to check if an input is a prime number
def is_prime(input):
    # chekcing if input is an integer
    if isinteger(input) == False:
        print("Invalid operand. Operand must be a positive integer.")
        return None
    else:
        # if not
        input = int(input)
        # checking if input is positive
        if input <= 0:
            print("Invalid operand. Operand must be a positive integer.")
            return None
        else:
            # checking if input is prime
            for i in range(2,input):
                if (input % i) == 0:
                    return False
                    break
            else:
                return True

# Defining a function to obtain LCM of two inputs
def LCM(input1,input2):
    # checking if both inputs are integers
    if isinteger(input1) == False or isinteger(input2) == False:
        print("Invalid operand(s). Both operands must be positive integers.")
        return None
    else:
        # if not
        input1 = int(input1)
        input2 = int(input2)
        # checking if both inputs are positive
        if input1 <= 0 or input2 <= 0:
            print("Invalid operand(s). Both operands must be positive integers.")
            return None
        # Checking which is greater
        elif input1 > input2:
            greatest = input1
        else:
            greatest = input2
        # Obtaining LCM, loops indefinitely until if condition is true
        while True:
            if greatest % input1 == 0 and greatest % input2 == 0:
                output = greatest
                break
            greatest = greatest + 1
        return output

# Defining a function to convert F temp to C temp or from C temp to F temp
def convert_temp(temp,convert_type):
    # checking if temp input is float or integer
    if isfloat(temp) == True or isinteger(temp) == True:
        # checking if conversion type is 'FtoC' or 'CtoF'
        if convert_type == "CtoF":
            output = float(temp * 1.8 + 32)
            return output
        elif convert_type == "FtoC":
            output = float((temp - 32) / 1.8)
            return output
        # if conversion type is not identified
        else:
            print('Invalid operand(s). The first operand must be an int or float. The second operand must be "FtoC" and "CtoF".')
            return None
    # if temp input is neither float nor integer
    else:
        print('Invalid operand(s). The first operand must be an int or float. The second operand must be "FtoC" and "CtoF".')
        return None

# Defining a function to get euclidean distance of two inputs
def get_euclidean_dist(input1,input2):
    # checking if both inputs are float or integer
    if isfloat(input1) == False and isinteger(input1) == False:
        print("Invalid operand(s). Both operands must be int or float.")
        return None
    elif isfloat(input2) == False and isinteger(input2) == False:
        print("Invalid operand(s). Both operands must be int or float.")
        return None
    # if both inputs are acceptable
    else:
        # calculation process
        output = float(((input1 ** 2) + (input2 ** 2)) ** 0.5)
        return output

# below are executions of the functions defined above

x = is_prime(5)
print(x)

x = is_prime(-0.5)
print(x)

x = LCM(5, 4)
print(x)

x = LCM(-4.3, "number")
print(x)

x = convert_temp(32, "FtoC")
print(x)

x = convert_temp(12.4, "nonsense")
print(x)

x = get_euclidean_dist(-3, 4)
print(x)

x = get_euclidean_dist(-4, "eight")
print(x)
