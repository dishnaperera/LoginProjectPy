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


# generating new password
def get_password(type_pw, length_pw):
    numbers_pw = string.digits
    symbols_pw = string.punctuation
    letters_pw = string.ascii_letters

    if type_pw == "a":
        result_pw = ''.join(random.choice(numbers_pw) for i in range(length_pw))
        print(result_pw)
    elif type_pw == "b":
        result_pw = ''.join(random.choice(symbols_pw) for i in range(length_pw))
        print(result_pw)
    elif type_pw == "c":
        result_pw = ''.join(random.choice(letters_pw) for i in range(length_pw))
        print(result_pw)


# getting user to choose self-made or generated Password.
source = input("Please enter a selection for your password \n "
               "1: if you would like and automatically generated password \n "
               "2: if you would like to select your own password")
if source == "1":
    type_pw = input("Please select what kind of password you would like generated: \n"
                    "a: Digits \n b: Symbols \n c: Letters ")
    length_pw = input("What length would you like the password to be? \n"
                      "Please select between 10 - 15 \n"
                      "or enter 'd' if you would like the default length to be selected.")
    if length_pw == "d":
        length_pw = 10
    get_password(type_pw, int(length_pw))

elif source == "2":
    result_pw = input("Please enter desired password:")
    print(result_pw)
