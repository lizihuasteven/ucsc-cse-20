'''
Student Name: Zihua Li
Assignment 4.1: Re-implementing built-in functions
This is a script that implements the following functions:
mybin, myoct, myround
Citation: No help from others received or used any resources to accomplish this assignment.
'''

'''
defining a function that is based on the built-in bin(...) function.
takes a decimal integer and returns the binary representation as a string,\
starting with '0b' followed by the actual binary notation.
'''
def mybin(input):
    # using a list to store each digit
    list = []
    # below using the dec-bin conversion principal
    # while input floor-divided by 2 is not zero
    while (input // 2) != 0:
        # append "input/2"'s remainder as an element to the list
        list.append(input % 2)
        # update input value after each calculation
        input = input // 2
    # when input is finally zero, the final stage
    else:
        list.append(input % 2)
    # reverse the order of the list because the binary value is stored reversely in the list
    list.reverse()
    # output: join all elements together as a string, no brackets, no commas
    output = "0b" + "".join(str(element) for element in list)
    return output

'''
defining a function that is based on the built-in oct(...) function.
takes a decimal integer and returns the octal representation as a string,
starting with '0o' followed by the actual octal notation.
'''
def myoct(input):
    # using a list to store each digit
    list = []
    # same theory as a the dec-bin conversion principal
    while (input // 8) != 0:
        list.append(input % 8)
        input = input // 8
    else:
        list.append(input % 8)
    # all the same
    list.reverse()
    output = "0o" + "".join(str(element) for element in list)
    return output

'''
defining a function that is based on the built-in round(...) function.
takes an integer or float and returns a rounded float value that 
is the number rounded to the second argument's decimal place.
'''
def myround(input1, input2):
    # using a list to store each digit (in str)
    list = [digit for digit in str(input1)]
    # if "number of digits up to which the given number is to be rounded" (input2) is positive
    if input2 > 0:
        # using list.index(element) to find the place where the element is stored in the list
        # if the digit that is about to be round up is more than 5, the digit before it will be add 1
        if int(list[list.index(".") + input2 + 1]) >= 5:
            list[list.index(".") + input2] = int(list[list.index(".") + input2]) + 1
        # deleting the decimal digits after round-up digit
        del list[list.index(".") + input2 + 1:]
        # output approach is same as in previous functions
        output = "".join(str(element) for element in list)
        return output
    # if "number of digits up to which the given number is to be rounded" (input2) is zero
    elif input2 == 0:
        # same theory, if digit > 5, previous digit + 1
        if int(list[list.index(".") + 1]) >= 5:
            list[list.index(".") - 1] = int(list[list.index(".") - 1]) + 1
        # deleting digits after the decimal dot
        del list[list.index(".") + 1:]
        # output, one thing different: manually adding a '0' after the decimal dot
        output = "".join(str(element) for element in list) + "0"
        return output
    # else condition, if input2 is negative
    else:
        # same theory
        if int(list[list.index(".") + input2]) >= 5:
            # attention!! wrote "+input2" instead of "-input2" is because input2 is negative!!!
            # a trap easy to fall into, spent an hour here trying to find out why output is incorrect
            # luckily, now it is clear :)
            list[list.index(".") + input2 - 1] = int(list[list.index(".") + input2 - 1]) + 1
        # a for loop to overwrite digits after the roundup digit into zero
        for element in list[list.index(".") + input2:list.index(".")]:
            if element != ".":
                list[list.index(element)] = "0"
        # below all the same, see previous comments
        del list[list.index(".") + 1:]
        output = "".join(str(element) for element in list) + "0"
        return output

# defining the main function for testing
def main(action, number):
    # what should be proceed
    if action == "mybin":
        # comparing outputs of mybin and bin with same input values
        return mybin(int(number)), bin(int(number))
    elif action == "myoct":
        return myoct(int(number)), oct(int(number))
    elif action == "myround":
        # the first test, also similarly
        t1arg1 = float(input("Please enter the number for the first test: "))
        t1arg2 = int(input("Please enter the digits for the first test: "))
        if float(myround(t1arg1,t1arg2)) == round(t1arg1,t1arg2):
            print("Congrats, the test has passed.")
        else:
            print("Error. Outputs are not persistent.")

# main function execution
if __name__ == "__main__":
    main()