'''
Student Name: Zihua Li
Assignment 6.1: Dictionary Practice
This is a script that implements the following functions:
dict_equal, count_words, morse
Citation: No help from others received or used any resources to accomplish this assignment.
'''

# dict001 & dict002 are dictionaries for testing
dict001 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
dict002 = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

# defining a function to compare two dictionaries are the same or not the same
def dict_equal(dict1,dict2):
    # indicator, once it is "1", means there are keys or values not the same
    indicator = 0
    # a for loop to check each item of two dictionaries
    for dict1_item, dict2_item in zip(dict1.items(), dict2.items()):
        # if there are difference
        if dict1_item != dict2_item:
            # indicator becomes "1"
            indicator = 1
    # if there are no differences
    if indicator == 0:
        return True
    # otherwise
    else:
        return False

# defining a function to count how many times do same word show up in a sentence
# and bring them up into a dictionary, key is the word, value is how many times
def count_words(sentence):
    # turning the input sentence into all lower case and deleting commas and dots
    sentence = sentence.lower().replace(",", "").replace(".", "")
    # creating a list "list_of_words" consists of the words in the sentence
    list_of_words = sentence.split()
    # creating an empty dictionary
    dict_words = {}
    # a for loop to examine each element in "list_of_words"
    for element in list_of_words:
        # if the element if found in dictionary
        if element in dict_words:
            # add 1 to the corresponding value
            dict_words[element] += 1
        # otherwise it is not found
        else:
            # creating a new key naming in the element, and make the value 1
            dict_words[element] = 1
    return dict_words

# defining a function to translate sentence into morse code
def morse(sentence):
    # morse code dictionary
    morse_dict = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
    }
    # turn the input sentence into all upper-case
    sentence = sentence.upper()
    # split each character of the sentence into a list
    sentence = [char for char in sentence]
    # creating list "morse_script" but by now it is empty
    morse_script = []
    # for each element in the list "sentence"
    for element in sentence:
        # if it is a blank space
        if element == " ":
            # append "/" into list "morse_script"
            morse_script.append("/")
        # otherwise
        else:
            # append the translation of that character into the list
            morse_script.append(morse_dict.get(element))
    # join all elements in list "morse_script" together with a blank space separating them
    output = " ".join(str(element) for element in morse_script)
    return output


# test executions
x = dict_equal(dict001, dict002)
print(x)

x = count_words("One fish, two fishes, red fish, blue fish")
print(x)

x = morse("Hello World")
print(x)