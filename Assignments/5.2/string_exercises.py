'''
Student Name: Zihua Li
Assignment 5.2: String Exercises
This is a script that implements following functions:
censor, fix_title, get_longest_word, frame
Citation: No help from others received or used any external resources to accomplish this assignment.
'''

# defining a function that censors keyword from a sentence and turn into stars
def censor(input1,input2):
    # if input2 is found in input1
    if input2 in input1:
        # determining number of stars by the number of characters of the word
        stars = len(input2) * "*"
        # replace input2 with stars in input1
        input1 = input1.replace(input2,stars)
    return input1

# defining a function that fix the title in various ways
def fix_title(input):
    # turn all characters of the input into lower case
    input = input.lower()
    # if a certain identifier is found in input string
    if "book:" in input:
        # delete the identifier from the input string
        input = input.replace("book:","")
        # using a python built-in function to turn the first character of each word into upper case
        input = input.title()
        return input
    elif "article:" in input:
        # same principal as above
        input = input.replace("article:","")
        # turn input into upper case
        input = input.upper()
        return input
    # if command is not identified
    elif ":" in input:
        # splitting the string into two, cutting in ':'
        input = input.split(":",1)
        # making the second element of the list
        input = str(input[1])
        # to be turned into lower case
        input = input.lower()
        return input

# defining a function to get the longest word in a sentence
def get_longest_word(input):
    # splitting the words into elements, storing in words_in_list
    words_in_list = input.split(" ")
    length_in_list = []
    # a for loop that makes the length of each word to be appended to length_in_list
    for word in words_in_list:
        length_in_list.append(len(word))
    # finding out which word is longest and returning it
    for word in words_in_list:
        if len(word) == max(length_in_list):
            return word

# defining a function that outputs a frame consists of words from sentence inputted
def frame(input):
    # splitting words from the sentence inputted
    words_in_list = input.split(" ")
    # variable 'space' only contains only one whitespace
    space = " "
    # printing the very first line and second, the first words is extracted from words_in_list
    print("*******\n*",words_in_list[0],space*(5-len(words_in_list[0])),"*\n",sep="",end="")
    # a pointer to record how many words are printed
    pointer = 1
    # using a while-loop to determine when to print out the very last line (cuz its different)
    while pointer < len(words_in_list)-1:
        # printing lines in the middle, number of spaces printed is determined by the length of word
        print("*",words_in_list[pointer],space*(5-len(words_in_list[pointer])),"*",sep="")
        pointer += 1
    else:
        # printing the very last line
        print("*",words_in_list[pointer],space*(5-len(words_in_list[pointer])),"*\n*******",sep="")
        # preventing the 'None' to be printed out at the end
        exit()

# below are executions
x = censor("apple banana orange","apple")
print(x)

x = fix_title("tRAsh:This IS NONSense")
print(x)

x = fix_title("ArtiCLE:commUNICatiON effICENt MachINE leaRNINg")
print(x)

x = fix_title("boOK:tHe gREat gatSBY")
print(x)

x = get_longest_word("There are some incredibly long words here")
print(x)

x = frame("one two three")
print(x)