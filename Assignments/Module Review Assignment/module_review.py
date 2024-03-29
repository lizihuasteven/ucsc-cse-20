'''
Student Name: Zihua Li
Module Review Assignment
This is a demo program that makes use of the 7 module elements that I described.
Citation: No help from others received or used any resources to accomplish this assignment.
'''

# importing os.path module
import os.path

# defining a function that checks whether inputted value is integer or not
def is_integer(input):
    try:
        int(input)
    except ValueError:
        return False
    return True

# defining the main function
def main():
    # greetings and menu options
    print("Welcome to Path Properties Toolbox!")
    print("You will be able to find out path properties in this program.")
    print("Menu:")
    print("\t1) Get absolute path")
    print("\t2) Check whether path exists or not")
    print("\t3) Get file size")
    print("\t4) Check whether inputted path is absolute or not")
    print("\t5) Check whether inputted path is a file or not")
    print("\t6) Check whether inputted path is a directory or not")
    print("\t7) Check whether inputted path is a symbolic link or not")
    # entering selected menu option
    what_to_do = input("Please enter what do you want to do, as a number (e.g. 1): ")
    # while entered menu option is not an integer, it is not acceptable data entry
    while is_integer(what_to_do) == False:
        # then indefinitely loop for asking for correct menu option
        print("Invalid input value, please enter again")
        what_to_do = input("Please enter what do you want to do, as a number (e.g. 1): ")
    else:
        # while entered menu option is <1 or >7, it is not available menu option
        while is_integer(what_to_do) == False or int(what_to_do) < 1 or int(what_to_do) > 7:
            # then indefinitely loop for asking for correct menu option
            print("Invalid input value, please enter again")
            what_to_do = input("Please enter what do you want to do, as a number (e.g. 1): ")
    # if user selected option 1
    if what_to_do == "1":
        # enter path
        path = input("Please enter relative path: ")
        # if does not exist
        while check_existence(path) == False:
            # error msg
            path = input("Path does not exist, please enter relative path again: ")
        # if exists
        else:
            # print out abs path
            print("The absolute path:", get_abspath(path))
        # return to main menu?
        return_home = input("Do you want to return to main menu, enter Y for yes, N for no: ")
        # if inputted value is not Y neither N (unacceptable option)
        while return_home != "Y" and return_home != "N":
            # asking again
            return_home = input("Do you want to return to main menu, enter Y for yes, N for no: ")
        # acceptable option
        else:
            # if Y
            if return_home == "Y":
                # return to main menu
                main()
            # if N
            elif return_home == "N":
                # exit program
                exit()
    # menu option 2
    elif what_to_do == "2":
        # path input
        path = input("Please enter path: ")
        # if not exist
        if check_existence(path) == False:
            # say not exist
            print("Path does not exist.")
        # exist
        else:
            # say exist
            print("Path exists.")
        # return to main menu?
        return_home = input("Do you want to return to main menu, enter Y for yes, N for no: ")
        # all the same as above
        while return_home != "Y" and return_home != "N":
            return_home = input("Invalid command, enter Y for yes, N for no: ")
        else:
            if return_home == "Y":
                main()
            elif return_home == "N":
                exit()
    # menu option 3
    elif what_to_do == "3":
        # same as above
        path = input("Please enter path: ")
        while check_existence(path) == False:
            path = input("Path does not exist, please enter path again: ")
        else:
            # if inputted path is not a file
            while is_file(path) == False:
                # say not a file, asking again for the path
                path = input("Path entered is not a file, please enter path again: ")
            # if it is a file
            else:
                # print out file size in bytes
                print("File size:", get_file_size(path), "byte(s).")
        # all the same as above
        return_home = input("Do you want to return to main menu, enter Y for yes, N for no: ")
        while return_home != "Y" and return_home != "N":
            return_home = input("Do you want to return to main menu, enter Y for yes, N for no: ")
        else:
            if return_home == "Y":
                main()
            elif return_home == "N":
                exit()
    # menu option 4
    elif what_to_do == "4":
        # same as above
        path = input("Please enter path: ")
        while check_existence(path) == False:
            path = input("Path does not exist, please enter path again: ")
        else:
            # if path inputted is not absolute
            if is_abs(path) == False:
                # say not absolute
                print("Path inputted is not absolute.")
            # if absolute
            else:
                # say absolute
                print("Path inputted is absolute.")
        # all the same as above
        return_home = input("Do you want to return to main menu, enter Y for yes, N for no: ")
        while return_home != "Y" and return_home != "N":
            return_home = input("Invalid command, enter Y for yes, N for no: ")
        else:
            if return_home == "Y":
                main()
            elif return_home == "N":
                exit()
    # menu option 5
    elif what_to_do == "5":
        # same as above
        path = input("Please enter path: ")
        while check_existence(path) == False:
            path = input("Path does not exist, please enter path again: ")
        else:
            # if inputted path is not a file
            if is_file(path) == False:
                # say it is not a file
                print("Path inputted is not a file.")
            # if it is a file
            else:
                # say it is a file
                print("Path inputted is a file.")
        # all the same as above
        return_home = input("Do you want to return to main menu, enter Y for yes, N for no: ")
        while return_home != "Y" and return_home != "N":
            return_home = input("Invalid command, enter Y for yes, N for no: ")
        else:
            if return_home == "Y":
                main()
            elif return_home == "N":
                exit()
    # menu option 6
    elif what_to_do == "6":
        # same as above
        path = input("Please enter path: ")
        while check_existence(path) == False:
            path = input("Path does not exist, please enter path again: ")
        else:
            # if path inputted is not a dir
            if is_dir(path) == False:
                # say it is not a dir
                print("Path inputted is not a directory.")
            # if it is a dir
            else:
                # say it is a dir
                print("Path inputted is a directory.")
        # all the same as above
        return_home = input("Do you want to return to main menu, enter Y for yes, N for no: ")
        while return_home != "Y" and return_home != "N":
            return_home = input("Invalid command, enter Y for yes, N for no: ")
        else:
            if return_home == "Y":
                main()
            elif return_home == "N":
                exit()
    # menu option 7
    elif what_to_do == "7":
        # same as above
        path = input("Please enter path: ")
        while check_existence(path) == False:
            path = input("Path does not exist, please enter path again: ")
        else:
            # if path inputted is a symbolic link
            if is_link(path) == False:
                # say it is a symbolic link
                print("Path inputted is not a symbolic link.")
            # if it is a symbolic link
            else:
                # say it is a symbolic link
                print("Path inputted is a symbolic link.")
        # all the same as above
        return_home = input("Do you want to return to main menu, enter Y for yes, N for no: ")
        while return_home != "Y" and return_home != "N":
            return_home = input("Invalid command, enter Y for yes, N for no: ")
        else:
            if return_home == "Y":
                main()
            elif return_home == "N":
                exit()

# defining a function which gets the relative path's absolute path
def get_abspath(path):
    # calling os.path module's abspath method, passing 'path' into the method
    abspath = os.path.abspath(path)
    # return absolute path
    return abspath

# defining a function which checks whether a path exists or not
def check_existence(path):
    # calling os.path module's exists method, passing 'path' into the method
    existence = os.path.exists(path)
    # if not exists
    if existence == False:
        return False
    # if exists
    else:
        return True

# defining a function which gets file size in bytes
def get_file_size(path):
    # calling os.path module's getsize method, passing 'path' into the method
    file_size = os.path.getsize(path)
    return file_size

# defining a function which checks whether a path is a file or not
def is_file(path):
    # calling os.path module's isfile method, passing 'path' into the method
    output = os.path.isfile(path)
    return output

# defining a function which checks whether a path is absolute or not
def is_abs(path):
    # calling os.path module's isabs method, passing 'path' into the method
    output = os.path.isabs(path)
    return output

# defining a function which checks whether a path is a directory or not
def is_dir(path):
    # calling os.path module's isdir method, passing 'path' into the method
    output = os.path.isdir(path)
    return output

# defining a function which checks whether a path is a symbolic link or not
def is_link(path):
    # calling os.path module's islink method, passing 'path' into the method
    output = os.path.islink(path)
    return output

# calling main function
if __name__ == "__main__":
    main()