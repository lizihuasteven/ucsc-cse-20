'''
Student Name: Zihua Li
Assignment 8.1: Loadable Contact List - Now as a Class!
This is a script that re-implements Assignment 6.2 (Assignment 6.2: Loadable Contact List) as a class,
with a few extra functions.
Citation: No help from others received or used any resources to accomplish this assignment.
'''

# creating a class contains the functionality of previous implementation in Assignment 6.2, plus some more methods.
class ContactList:
    # this is the constructor
    def __init__(self, file_name):
        # a method that loads the contact list file and creates dictionary which has the content of the file
        def load_contact_list(file_name):
            # creating a dictionary
            contact_dict = {}
            # opening the file in read-only mode
            contact_list = open(file_name, "r")
            # a for-loop to append each info as key and value into the higher-level dict and lower-level dict
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
        # initializing variables
        self.__contact_dict = load_contact_list(file_name)
        self.__file_name = file_name

    # defining a method to get the email of a person
    def get_email(self, name):
        # if this person's name is found in contact list dictionary
        if name in self.__contact_dict:
            # return this person's email
            return self.__contact_dict[name]["email"]
        # if not found
        else:
            print("Error: Name not found.")
            return None

    # defining a method to get the phone number of a person
    def get_phone(self, name):
        # almost the same as in function get_email
        if name in self.__contact_dict:
            return self.__contact_dict[name]["phone"]
        else:
            print("Error: Name not found.")
            return None

    # defining a method to get the address of a person
    def get_address(self, name):
        # almost the same as in function get_email
        if name in self.__contact_dict:
            return self.__contact_dict[name]["address"]
        else:
            print("Error: Name not found.")
            return None

    # defining a method to get a list of emails of a list of people's names
    def get_email_list(self, name_list):
        # creating a list for storing emails that match target
        email_list = []
        # a for loop to find whether each person's name can be found in the contact list dictionary
        # and get append each person's email into list email_list
        for name in name_list:
            # if the person's name is not found
            if name not in self.__contact_dict:
                print("Error:", name, "is not found in the contact list dictionary.")
            else:
                # appending that person's email into list email_list
                email_list.append(self.__contact_dict[name]["email"])
        return email_list

    # defining a method to get a list of phone numbers of a list of people's names
    def get_phone_list(self, name_list):
        # almost the same as in function get_email_list
        phone_list = []
        for name in name_list:
            if name not in self.__contact_dict:
                print("Error:", name, "is not found in the contact list dictionary.")
            else:
                phone_list.append(self.__contact_dict[name]["phone"])
        return phone_list

    # defining a method to get a list of addresses of a list of people's names
    def get_address_list(self, name_list):
        # almost the same as in function get_email_list
        address_list = []
        for name in name_list:
            if name not in self.__contact_dict:
                print("Error:", name, "is not found in the contact list dictionary.")
            else:
                address_list.append(self.__contact_dict[name]["address"])
        return address_list

    # defining a method that adds a tuple of contact information into private dictionary "contact_dict"
    def add_contact(self, info_tuple):
        # a pointer that indicates which element of the tuple have we gone for so
        pointer = 0
        # a for loop to insert each element into the dict
        for element in info_tuple:
            # if it is 0, means it is the first element, so it is the name
            # firstly creat the key and create an empty dictionary in its value
            if pointer == 0:
                self.__contact_dict[element] = {}
                pointer += 1
                continue
            # and so on
            if pointer == 1:
                self.__contact_dict[info_tuple[0]]["email"] = element
                pointer += 1
                continue
            # and so on
            if pointer == 2:
                self.__contact_dict[info_tuple[0]]["phone"] = element
                pointer += 1
                continue
            # and so on
            if pointer == 3:
                self.__contact_dict[info_tuple[0]]["address"] = element
        return self.__contact_dict

    # defining a method that removes the contact information of the person with name taken in
    def remove_contact(self, name):
        self.__contact_dict.pop(name)

    # defining a method that gets all of the names in the private dictionary
    def get_all_names(self):
        # creating a list that will be used to store all the names
        all_names = []
        # a for loop to store each name into list "all_names"
        for name in self.__contact_dict:
            all_names.append(name)
        # returning the list
        return all_names

    # and so on
    def get_all_emails(self):
        all_emails = []
        for name in self.__contact_dict:
            all_emails.append(self.__contact_dict[name]["email"])
        return all_emails

    # and so on
    def get_all_phones(self):
        all_phones = []
        for name in self.__contact_dict:
            all_phones.append(self.__contact_dict[name]["phone"])
        return all_phones

    # and so on
    def get_all_addresses(self):
        all_addresses = []
        for name in self.__contact_dict:
            all_addresses.append(self.__contact_dict[name]["address"])
        return all_addresses

    # defining a method that prints out the name of each person and their contact information
    def display(self):
        for name in self.__contact_dict:
            # print the name, email, phone, and address
            print(name, "\t", self.__contact_dict[name]["email"], "\t", self.__contact_dict[name]["phone"], "\t",
                  self.__contact_dict[name]["address"], sep="")

    # this magic method returns a string representation of the contact list.
    def __str__(self):
        # a list that stores all names
        list_of_names = []
        # for each name in the dictionary
        for name in self.__contact_dict:
            # appending names into the list
            list_of_names.append(name)
        # returning the length of the list (how many names)
        # and using function "".join() to join the elements of the list together without the brackets
        return "Contacts (" + str(len(list_of_names)) + "): " + ", ".join(list_of_names) + "."


# main function for testing
def main():
    instance = ContactList("sample_contact_list.txt")
    print(instance.get_email("Sandy Cheeks"))
    print(instance.get_phone("Sandy Cheeks"))
    print(instance.get_address("Sandy Cheeks"))
    print(instance.get_email_list(["Sandy Cheeks", "Avatar Aang"]))
    print(instance.get_phone_list(["Sandy Cheeks", "Avatar Aang"]))
    print(instance.get_address_list(["Sandy Cheeks", "Avatar Aang"]))
    instance.add_contact(("Zihua Li", "zli487@ucsc.edu", "831-226-6820", "1410 Ocean Street"))
    print(instance.get_all_names())
    print(instance.get_all_emails())
    print(instance.get_all_phones())
    print(instance.get_all_addresses())
    instance.display()
    print(instance.__str__())

if __name__ == "__main__":
    main()