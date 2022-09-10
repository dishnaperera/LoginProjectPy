# Dishna Perera 6th September 2022
# Program to allow login for existing users, creation of new accounts for new users,
# and access user and login information

import string
import random

# Reading in file with current account and allowing writing to file.
currentAccounts = open('accounts.txt', 'r+').readlines()

# Adding usernames and password from file into dictionary with the two values.
accounts = {}
for line in currentAccounts:
    parts = line.strip().split(" ")
    user = parts[0]
    password = parts[1]
    accounts[user] = password

def menu():
    # Displaying welcome menu to user
    menuIn = input("Welcome! Please select an option from the choices below: /n"
                   "a: Login /n"
                   "b: Register /n"
                   "c: Save file /n"
                   "d: View Accounts /n"
                   "e: Exit")
    if menuIn == "a":
        login()
    if menuIn == "b":
        save_file()
    if menuIn == "c":
        save_file()
    if menuIn == "d":
        save_file()
    if menuIn == "e":
        save_file()


# •	Login – for users who have previously registered. Username and password to be checked for validity.
# •	Register – create a new user account.
# •	Passwords – new users given the option to enter their own password or generate one.
# •	Generated passwords – user given the option to choose the password character types –
# numbers, symbols or letters. The default password length should be applied, but users
# should also be allowed to choose how many characters
# •	Save file – usernames and passwords should be saved to a text file accounts.txt
# •	Exit – delay for 2 seconds before exit
# •	View accounts – to display user account information from the accounts.txt file
# (assuming that only admin have access to this program).

def login():
    username = input("Enter Username")
    if username in accounts:
        password = input("Enter Password")
        if password == accounts[username]:
            print("Password is correct")
        else:
            print("password is incorrect")
    else:
        print("Username does not exist")




def register():
    # asking customer for username input
    username = input("Please enter your preferred username ")
    password = get_password(type_pw, length_pw)
    accounts[username] = password


# generating new password
def get_password():
    numbers_pw = string.digits
    symbols_pw = string.punctuation
    letters_pw = string.ascii_letters

    source = input("Please enter a selection for your password \n "
                   "1: if you would like and automatically generated password \n "
                   "2: if you would like to select your own password")
    if source == "1":
        type_pw = input("Please select what kind of password you would like generated: \n"
                        "a: Digits \n b: Symbols \n c: Letters ")
        # length_pw = input("What length would you like the password to be? \n"
        #                   "Please select between 10 - 15 \n"
        #                   "or enter 'd' if you would like the default length to be selected.")
        while True:
            length_pw = input("What length would you like the password to be? \n"
                              "Please select between 10 - 15 \n"
                              "or enter 'd' if you would like the default length to be selected.")
            if int(length_pw) < 10 and int(length_pw) > 15 and not "d":
                print("Number entered was not valid, Please select a number between 10 - 15 \n"
                      "or enter 'd' if you would like the default length to be selected.")
            else:
                break
            # length_pw = (int(length_pw) < 10);
            # print("Please enter number that is 10 or greater")
            # length_pw = input("What length would you like the password to be? \n"
            #                   "Please select between 10 - 15 \n"
            #                   "or enter 'd' if you would like the default length to be selected.")
        if length_pw == "d":
            length_pw = 10

        # while True:
        #     length_pw = (int(length_pw) < 10);
        #     print("Please enter number that is 10 or greater")
    elif source == "2":
        result_pw = input("Please enter desired password:")
        print(result_pw)

    if type_pw == "a":
        result_pw = ''.join(random.choice(numbers_pw) for i in range(int(length_pw)))
        print(result_pw)
    elif type_pw == "b":
        result_pw = ''.join(random.choice(symbols_pw) for i in range(int(length_pw)))
        print(result_pw)
    elif type_pw == "c":
        result_pw = ''.join(random.choice(letters_pw) for i in range(int(length_pw)))
        print(result_pw)

    # getting user to choose self-made or generated Password.

get_password()



def save_file():
    with open ("accounts2.txt", "w") as f:
        for u_name in accounts.keys():
            f.write(u_name + " " +  accounts[u_name] + "\n")


