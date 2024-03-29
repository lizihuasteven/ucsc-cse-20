'''
Student Name: Zihua Li
Assignment 3.3: String Toolbox
This is a script that implements the following functions:
parse_string, get_string_length, and reverse_string.
Citation: No help from others received or used any resources to accomplish this assignment.
'''

def is_len(input):
    try:
        len(input)
    except TypeError:
        return False
    return True

'''
Defining a function that returns a new string that is a copy of the first argument 
up until the first occurrence of the second argument; if the second argument is not 
found in the original first argument, the function returns the entire first argument.
'''
def parse_str(input1,input2):
    # checking if inputs are acceptable
    if is_len(input1) == False or is_len(input2) == False:
        print("Invalid argument(s). parse_str takes a string argument and a character argument.")
        return None
    # checking if input1 is one character
    elif len(input2) != 1:
        print("Invalid argument(s). parse_str takes a string argument and a character argument.")
        return None
    else:
        # a for loop to print each character in char_in_list until input2 detected
        char_in_list = [char for char in input1]
        for char in char_in_list:
            if char == input2:
                exit()
            else:
                print(char,end = "")

# Defining a function that returns the length of the input string
def get_string_length(input):
    # counter for the length of the string
    counter = 0
    # checking if input is acceptable
    if is_len(input) == False:
        print("Invalid argument(s). get_string_length takes one string argument.")
    else:
        # if input is acceptable, run a for loop to count length of the string
        for i in input:
            counter = counter + 1
        return counter

# Defining a function that returns a new string that is the reverse of the input string
def reverse_string(input):
    # checking if input is acceptable
    if is_len(input) == False:
        print("Invalid argument(s). reverse_string takes one string argument.")
        return None
    else:
        # determining the length of the input string
        length = len(input)
        char_in_list = [char for char in input]
        # reverse the order of the list
        reversed_list = char_in_list[::-1]
        # join the elements together without brackes and commas
        output = "".join(str(element) for element in reversed_list)
        return output

# below are executions of the functions defined above

x = get_string_length("hello world")
print(x)
x = get_string_length(5)
print(x)
x = reverse_string("hello world")
print(x)
x = parse_str("one message*two message", "*")
print(x)