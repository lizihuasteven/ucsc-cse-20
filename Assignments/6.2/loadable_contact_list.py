'''
Student Name: Zihua Li
Assignment 6.2: Loadable Contact List
This is a script that implements the following functions:
load_contact_list, get_email, get_phone, get_address, get_email_list, get_phone_list, get_address_list
Citation: "How do I remove \n from my python dictionary?"
           answer by "thefourtheye"
           https://stackoverflow.com/questions/22890673/how-do-i-remove-n-from-my-python-dictionary
'''

# defining a function to load the information in a file into a dictionary and return it
def load_contact_list(file_name):
    # creating a dictionary
    contact_dict = {}
    # opening the file in read-only mode
    contact_list = open(file_name, "r")
    # a for-loop to append each info as key and value into the higher-level dictionary and lower-level dictionary
    for line in contact_list:
        # splitting the key and values and preventing "\n" at the end of line
        key, value1, value2, value3 = line.rstrip("\n").split(", ")
        # creating a temporary dictionary to store email, phone, address as keys
        # and their values as values of the dictionary
        temp_value_dict = {}
        temp_value_dict["email"] = value1
        temp_value_dict["phone"] = value2
        temp_value_dict["address"] = value3
        # appending the temporary dictionary into the value of key of the main dictionary
        contact_dict[key] = temp_value_dict
    # closing the file
    contact_list.close()
    return contact_dict

# defining a function to get the email of a person in the 2nd argument
def get_email(contact_list_dict, name):
    # if this person's name is found in contact list dictionary
    if name in contact_list_dict:
        # return this person's email
        return contact_list_dict[name]["email"]
    # if not found
    else:
        print("Error: Name not found.")
        return None

# defining a function to get the phone number of a person in the 2nd argument
def get_phone(contact_list_dict, name):
    # almost the same as in function get_email
    if name in contact_list_dict:
        return contact_list_dict[name]["phone"]
    else:
        print("Error: Name not found.")
        return None

# defining a function to get the address of a person in the 2nd argument
def get_address(contact_list_dict, name):
    # almost the same as in function get_email
    if name in contact_list_dict:
        return contact_list_dict[name]["address"]
    else:
        print("Error: Name not found.")
        return None

# defining a function to get a list of emails of a list of people's names in the 2nd argument
def get_email_list(contact_list_dict, name_list):
    # creating a list for storing emails that match target
    email_list = []
    # a for loop to find whether each person's name can be found in the contact list dictionary
    # and get append each person's email into list email_list
    for name in name_list:
        # if the person's name is not found
        if name not in contact_list_dict:
            print("Error:", name, "is not found in the contact list dictionary.")
        else:
            # appending that person's email into list email_list
            email_list.append(contact_list_dict[name]["email"])
    return email_list

# defining a function to get a list of phone numbers of a list of people's names in the 2nd argument
def get_phone_list(contact_list_dict, name_list):
    # almost the same as in function get_email_list
    phone_list = []
    for name in name_list:
        if name not in contact_list_dict:
            print("Error:", name, "is not found in the contact list dictionary.")
        else:
            phone_list.append(contact_list_dict[name]["phone"])
    return phone_list

# defining a function to get a list of addresses of a list of people's names in the 2nd argument
def get_address_list(contact_list_dict, name_list):
    # almost the same as in function get_email_list
    address_list = []
    for name in name_list:
        if name not in contact_list_dict:
            print("Error:", name, "is not found in the contact list dictionary.")
        else:
            address_list.append(contact_list_dict[name]["address"])
    return address_list
