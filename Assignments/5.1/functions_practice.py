'''
Student Name: Zihua Li
Assignment 5.1: Functions Practice
This is a script that implements following functions:
simple_sum, assign_grade, num_of_words, find_average
Citation: No help from others received or used any external resources to accomplish this assignment.
'''

# defining a function that takes two input arguments and returns the sum
def simple_sum(input1,input2):
    output = input1 + input2
    return output

# defining a function takes in number of points and returns a string grade
def assign_grade(input):
    # checking if input is within the criteria
    if input > 100 or input < 0:
        print("Inputted points cannot be negative or above 100.")
        return None
    else:
        # following are if-conditions that checks which grade should be assigned
        if input >= 90:
            output = "A"
            return output
        elif input >= 80:
            output = "B"
            return output
        elif input >= 70:
            output = "C"
            return output
        elif input >= 60:
            output = "D"
            return output
        elif input < 60:
            output = "F"
            return output

# defining a function that takes in a sentence and returns the number of words in the sentence
def num_of_words(input):
    # creating a list that stores each character in the sentence as an element
    char_in_list = [char for char in input]
    counter = 0
    # a for-loop that counts how many elements of whitespace are in the list
    for char in char_in_list:
        if char == " ":
            counter += 1
    # if there are x whitespaces, then there will be x+1 words
    counter += 1
    return counter

# defining a function that takes in a list of numbers and returns the average
def find_average(input_list):
    # counting how many elements are in the list
    num_of_elements = len(input_list)
    sum = 0
    # a for loop that adds up all of the elements in the list
    for element in input_list:
        sum += element
    # calculating average number
    average = sum / num_of_elements
    return average

x = simple_sum(10,20)
print(x)

x = assign_grade(60)
print(x)

x = num_of_words("abc xyz we are living")
print(x)

x = find_average([10,20,30])
print(x)